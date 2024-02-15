from django.contrib.auth.tokens import PasswordResetTokenGenerator

#from six import text_text

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self,user,timestamp):
        return (
        text_text(user.pk) + text_text(timestamp) 
        # text_type(user.profile.signup_confirmation)
        )

generate_token = TokenGenerator()