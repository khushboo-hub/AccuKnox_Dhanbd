from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.utils.timezone import now
from .models import CustomUser
import logging

# Setup logging
logger = logging.getLogger(__name__)


@receiver(user_logged_in)
def update_logged_in(sender, request, user, **kwargs):
    if isinstance(user, CustomUser):
        # Debugging print statement (temporary)
        print(f"User {user.email} logged in at {now()}")

        # Logging (recommended)
        logger.info(f"User {user.email} logged in at {now()}")

        user.logged_in = now()
        user.save()
