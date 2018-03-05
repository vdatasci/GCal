def add_event():
  """Add an event using the Google Calendar API.

  Creates a Google Calendar API service object
  and creates a new event on the user's calendar.
  """
  credentials = get_credentials()
  http = credentials.authorize(httplib2.Http())
  service = discovery.build('calendar', 'v3', http=http)

  body = {
    u'status': u'confirmed',
    u'kind': u'calendar#event',
    u'start': {u'dateTime': u'2015-08-19T10:00:00+02:00'},
    u'end': {u'dateTime': u'2015-08-19T10:50:00+02:00'},
    u'summary': u'jeremy test event summary',
    u'organizer': {u'self': True, u'displayName': u'Jeremy Tammik', u'email': u'jeremytammik@gmail.com'},
    u'creator': {u'self': True, u'displayName': u'Jeremy Tammik', u'email': u'jeremytammik@gmail.com'}
  }
  service.events().insert( calendarId='primary', body=body).execute()
