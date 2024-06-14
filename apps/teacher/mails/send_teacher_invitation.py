from django.core.mail import send_mail


def send_teacher_mail(
        to: str,
        teacher_email: str,
        teacher_name: str,
        classroom_name: str,
        invitation_sub_code: str,
        invitation_accept_code: str
    ):
    send_mail(
        subject=f'[LearnHub] - Invitación para ser profesor',
        message=f'La invitación es de \"{teacher_name}\" para ser profesor en \"{classroom_name}\".\n Ingrese a este enlace para aceptar la invitación: http://localhost:3000/w/classroom/invitations?subCode={invitation_sub_code}&acceptCode={invitation_accept_code}',
        from_email=teacher_email,
        recipient_list=[to],
        fail_silently=False
    )
