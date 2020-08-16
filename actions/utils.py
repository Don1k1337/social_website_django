import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .models import Action


# Shortcut func that will allow to create
# a new Action obj in a simple way
def create_action(user, verb, target=None):
    # check for any similar action made in the last minute
    # returning timezone-aware object by timezone.now()
    now = timezone.now()
    # to store the datetime from 1 min ago
    # and retrieving identical actions performed by the
    # user since then
    last_minute = now - datetime.timedelta(seconds=60)
    similar_actions = Action.objects.filter(user_id=user.id,
                                            verb=verb,
                                            created__gte=last_minute)
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(target_ct=target_ct,
                                                 target_id=target.id)
    if not similar_actions:
        # no existing actions found
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True
    # otherwise
    return False

