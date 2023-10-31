import datetime
from collections import defaultdict
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .models import Match


def index(request):
    if request.method == "GET":
        date = datetime.datetime.now().date()
        unique_countries = Match.objects.order_by('country').values_list('country', flat=True).distinct()
        context = {
            'unique_countries': unique_countries,
            'date': date
        }
        return render(request, 'bets/home.html', context)


def match_list(request):
    if request.method == 'GET':
        selected_country = request.GET.get('country', 'No Country')
        picked_date = request.GET.get('date')
        date = datetime.datetime.strptime(picked_date, '%Y-%m-%d').date()
        result_list = []

        filtered_matches = Match.objects.filter(start_date__date=date, country=selected_country)

        if filtered_matches:
            # Create a defaultdict to store matches by league
            matches_by_league = defaultdict(list)

            # Group matches by the 'league' field
            for match in filtered_matches:
                matches_by_league[match.competition].append({
                    'home_team': match.home_team,
                    'away_team': match.away_team,
                    'start_date': match.start_date,
                    'prediction': match.prediction,
                    'result': match.result,
                    'status': match.status,
                    'odds': match.odds,
                    'bet': match.bet,
                })

            # Convert the defaultdict to a list of dictionaries
            result_list = [{'competition': league, 'matches': matches} for league, matches in matches_by_league.items()]

        context = {
            'result_list': result_list,
            'selected_country': selected_country,
        }
        html_response = render_to_string('bets/matches.html', context)

        # Return the HTML content as a string in the JsonResponse
        return HttpResponse(html_response)



