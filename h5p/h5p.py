"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer
from xblock.fragment import Fragment

from django.template import Context, Template

from random import shuffle


class Cards(object):
    """docstring for Cards"""

    width = 100
    heigth = 100

    def __init__(self, img_url, Card_id):
        super(Cards, self).__init__()
        self.img_url = img_url
        self.Card_id = Card_id


class H5pXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.

    numberCards = 2

    allCards = []

    for card in range(numberCards):
        NewCard = Cards("https://h5p.org/sites/default/files/h5p/content/708/images/card-5371ceb6aa92b.jpg", card)
        allCards.append(NewCard)
        allCards.append(NewCard)

    shuffle(allCards)

    result = Integer(
        default=0, scope=Scope.user_state,
        help="The result for each user or student"
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the H5pXBlock, shown to students
        when viewing courses.
        """
        template_str = self.resource_string("static/html/h5p.html")
        template = Template(template_str)
        html = template.render(Context({

            'cardList': self.allCards,
            'allCards': self.result,

            }))
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/h5p.css"))
        frag.add_javascript(self.resource_string("static/js/src/h5p.js"))
        frag.initialize_js('H5pXBlock')
        return frag

    # TO-DO:change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """

        if data['result'] == 'success':
            self.result += 1
        else:
            self.result -= 1

        # Just to show data coming in...
        return {'result': self.result}
        # Just to show data coming in...

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("H5pXBlock",
             """<vertical_demo>
                <h5p/>
                </vertical_demo>
             """),
        ]
