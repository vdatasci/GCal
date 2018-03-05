from oauth2client.client import flow_from_clientsecrets

statdir = '''/home/lemur/Python/project/GCal/static'''

flow = flow_from_clientsecrets( statdir + '/client_secret.json',
                               scope='https://www.googleapis.com/auth/calendar',
                               redirect_uri='http://example.com/auth_return')


auth_uri = flow.step1_get_authorize_url()

#########


