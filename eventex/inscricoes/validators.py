from django.core.exceptions import ValidationError


def valida_cpf(value):
    if not value.isdigit():
        raise ValidationError('cpf deve conter apenas numeros, verifique!', 'digito')

    if len(value) != 11:
        raise ValidationError('cpf deve conter 11 digitos, verifique!','tamanho')
