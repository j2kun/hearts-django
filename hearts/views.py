from rest_framework.decorators import api_view

import hearts.models as models


@api_view(['GET', 'POST'])
def index(request):
    # return templated response
    pass
