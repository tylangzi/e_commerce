from django.http import JsonResponse


def JR(response_date):
    return JsonResponse(response_date, json_dumps_params={'ensure_ascii': False})
