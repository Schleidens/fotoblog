from django.core.exceptions import ValidationError

class containLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'your password should contain letter',
                code='password_no_letter'
            )

    def get_help_text(self):
        return 'Your password should contain one letter min'