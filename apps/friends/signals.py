from django.dispatch import Signal


follower_created = Signal()
follower_removed = Signal()
followee_created = Signal()
followee_removed = Signal()
following_created = Signal()
following_removed = Signal()