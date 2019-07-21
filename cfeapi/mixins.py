from django.http import JsonResponse


class JsonResponseMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(context, **response_kwargs)

    def get_data(self, context):
        return context
