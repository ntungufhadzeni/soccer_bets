from django.db import models
from django.utils import timezone


class Match(models.Model):
    id = models.IntegerField(editable=False, primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    country = models.CharField(max_length=50)
    competition = models.CharField(max_length=50)
    home_team = models.CharField(max_length=50)
    away_team = models.CharField(max_length=50)
    bet = models.CharField(max_length=100)
    odds = models.JSONField(null=True, blank=True)
    status = models.CharField(max_length=20)
    result = models.CharField(max_length=10)
    start_date = models.DateTimeField()
    last_update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Matches'
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.home_team} vs. {self.away_team} ({self.start_date.strftime('%B %d, %Y %H:%M')})"

    @property
    def prediction(self):
        if self.bet == '1':
            return self.home_team
        elif self.bet == 'X':
            return 'X'
        elif self.bet == '2':
            return self.away_team
        elif self.bet == '1X':
            return f'{self.home_team} or X'
        elif self.bet == 'X2':
            return f'X or {self.away_team}'
        elif self.bet == '12':
            return f'{self.home_team} or {self.away_team}'
        else:
            return self.bet



