class LazinessError(Exception):
    def __init__(self, message, email):
        self.message = "%s - sending email to %s.  (WARNING: failed to send email to %s. Sending email has not yet been implemented)" % (message, email, email)

    def __str__(self):
        return self.message
