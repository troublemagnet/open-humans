from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.db import models

from common import fields
from data_import.models import BaseDataFile, DataRetrievalTask

from ..models import BaseStudyUserData


class UserData(BaseStudyUserData):
    """
    Represents the user data for one American Gut participant.
    """

    class Meta:
        verbose_name = 'American Gut user data'
        verbose_name_plural = verbose_name

    user = fields.AutoOneToOneField(settings.AUTH_USER_MODEL,
                                    related_name='american_gut')

    text_name = 'American Gut'
    href_connect = 'https://www.microbio.me/AmericanGut/authed/open-humans/'
    href_add_data = 'https://www.microbio.me/AmericanGut/authed/open-humans/'
    href_learn = 'http://americangut.org/'
    retrieval_url = reverse_lazy('studies:american-gut:request-data-retrieval')
    msg_add_data = ("We don't have any survey IDs that we can add "
                    'data for. You can add survey IDs through the American '
                    'Gut website.')

    @property
    def survey_ids(self):
        try:
            return self.data.get('surveyIds', [])
        except AttributeError:
            return []

    @property
    def msg_curr_data(self):
        return ('Current survey IDs: %s. ' % ','.join(self.survey_ids) +
                '<a href="%s">Go to American Gut</a> ' % self.href_add_data +
                'to add more.')

    @property
    def has_key_data(self):
        """
        Return false if key data needed for data retrieval is not present.
        """
        return self.is_connected and self.survey_ids


class DataFile(BaseDataFile):
    """
    Storage for an American Gut data file.
    """

    class Meta:
        verbose_name = 'American Gut data file'

    user_data = models.ForeignKey(UserData)
    task = models.ForeignKey(DataRetrievalTask,
                             related_name='datafile_american_gut')

    def __unicode__(self):
        return '%s:%s:%s' % (self.user_data.user, 'american_gut', self.file)
