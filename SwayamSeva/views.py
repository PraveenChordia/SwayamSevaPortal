from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from SwayamSeva.forms import RegistrationForm, LoginForm, ApplicationForm
from SwayamSeva.IndirectUseFiles.doc_forms import *
from SwayamSeva.models import CompleteUserDetails, UserDetails, Schemes
from SwayamSeva.IndirectUseFiles.token import account_activation_token
from SwayamSevaPortal import settings


def home_view(request):
    return render(request, 'home.html')


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.username)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data['email']
            email = EmailMessage(
                mail_subject, message, settings.EMAIL_HOST_USER, [to_email]
            )
            if not email.send():
                msg = '''Email Could Not be send. Please try again Later :('''
                context['notice'] = msg
                return render(request, 'notice.html', context)
            msg = '''Please confirm your email address to complete the 
            registration'''
            context['notice'] = msg
            return render(request, 'notice.html', context)
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', {'form': form})


def activate_view(request, uidb64, token):
    context = {}
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserDetails.objects.get(username=uid)
    except(TypeError, ValueError, OverflowError, UserDetails.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        msg = '''Thank you for your email confirmation. 
        Now you can login your account.'''
        context['notice'] = msg
        return render(request, 'notice.html', context)
    else:
        msg = '''Activation link is invalid!'''
        context['notice'] = msg
        return render(request, 'notice.html', context)


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('schemes')
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            aadhaar = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=aadhaar, password=password)
            if user:
                login(request, user)
                return redirect('schemes')
    else:
        form = LoginForm()

    context['login_form'] = form
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def schemes_view(request):
    return render(request, 'schemes.html')


def apply_view(request, scheme):
    context = {'scheme': scheme}
    if request.user.is_authenticated:
        user = UserDetails.objects.get(username=request.user.username)
        try:
            udid = user.CUD_set.UDid
            cuduser = CompleteUserDetails.objects.get(UDid=udid)
        except ObjectDoesNotExist:
            cuduser = None
        default = {
            'Aadhaar': request.user.username,
            'F_name': request.user.first_name,
            'L_name': request.user.last_name
        }
        if request.POST:
            if cuduser:
                form = ApplicationForm(request.POST, initial=default, instance=cuduser)
            else:
                form = ApplicationForm(request.POST, initial=default)
                save = True

            if form.is_valid():
                user = form.save(commit=False, )
                user.save()
                return redirect('docs', scheme)
            else:
                context['Application-form'] = form

        else:
            form = ApplicationForm(initial=default, instance=cuduser)
            context['Application-form'] = form
        return render(request, 'application.html', {'form': form, 'context': context})
    else:
        return redirect('login')


def docs_view(request, scheme):
    context = {'scheme': scheme}
    default = {}
    if request.user.is_authenticated:
        user = UserDetails.objects.get(username=request.user.username)
        user_id = {'Name': request.user.first_name + ' ' + request.user.last_name, 'Aadhaar': request.user.username}
        try:
            udid = user.CUD_set.UDid
            default['Uid'] = udid
        except ObjectDoesNotExist:
            return redirect('apply', scheme)

        formfunc = 'doc' + scheme

        if request.POST:
            defform = defForm(request.POST, initial=user_id)
            form = globals()[formfunc](request.POST, initial=default)
            if form.is_valid():
                application = form.save(commit=False)
                try:
                    savescheme = Schemes.objects.create(Scheme_Name=scheme, Aadhaar=user)
                    savescheme.save()
                    application.save()
                    msg = '''Your Application Has been submitted.
                                    Our officials will reach out to you soon.'''
                except Exception:
                    msg = f'''You Hava already Applied for the {scheme} scheme.'''

                context['notice'] = msg
                return render(request, 'notice.html', context)
            else:
                context['form'] = form
        else:
            defform = defForm(initial=user_id)
            form = globals()[formfunc](initial=default)
            context['form'] = form
        return render(request, 'apply/docs.html', {'form': form, 'defform': defform, 'context': context})
    else:
        return redirect('login')


def return_view(request, context):
    msg = context[2:-2].split(':')
    return render(request, 'notice.html', {'notice': msg[1]})


def profile_view(request):
    context = {}
    if request.user.is_authenticated:
        context['user'] = UserDetails.objects.get(username=request.user.username)
        return render(request, 'profile.html', context)
    else:
        return redirect('login')
