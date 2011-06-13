from hashlib import md5
from urllib import urlencode,quote

from django import template
from eze_auth.settings import EZENGAGE_APP_DOMAIN,EZENGAGE_TOKEN_CB

register = template.Library()

@register.simple_tag
def eze_login_widget(redirect_to, style=None, width=None, height=None):
    """
    Generates a eze login widget

    Syntax::

        {% eze_login_widget <redirect_to> [style] [width] [height] %}

    Example::

        {% eze_login_widget "http://example.com/token_cb/" "normal" 400 190 %}
    """

    #TODO: make this configable
    container_id = 'eze-login-widget-container'
    token_cb = EZENGAGE_TOKEN_CB + '?next=' + quote(redirect_to)

    html =  [
        "<div id='%s'></div>" %container_id,
        "<script type='text/javascript'>",
        "  var ezengage_app_domain = '%s';" % EZENGAGE_APP_DOMAIN,
        "  var ezengage_token_cb = '%s';" % token_cb
    ]
    if style != None:
        html.append("   var ezengage_widget_style = '%s';" %style)
    if width != None:
        html.append("   var ezengage_widget_width = '%s';" %width)
    if height != None:
        html.append("   var ezengage_widget_height = '%s';" %width)
    html.append("   var ezengage_container_id = '%s';" %container_id)
    html.append('''
        (function() {
            var ezc = document.createElement('script'); ezc.type = 'text/javascript'; ezc.async = true;
            ezc.src = 'http://' + ezengage_app_domain + '.ezengage.net/login/embed.js';
            (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ezc);
        })();
    </script>
    ''')

    return '\n'.join(html)
