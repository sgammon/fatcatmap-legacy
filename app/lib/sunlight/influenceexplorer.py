"""
The influenceexplorer module provides API wrappers for the data provided on
InfluenceExplorer.com.
"""


import urllib2
import urllib
try:
    import json
except ImportError:
    import simplejson as json

from transparencydata import DEFAULT_URL


# defaults of None don't mean that there is not default or no limit--
# it means that no parameter will be sent to the server, and the server
# will use its own default.
DEFAULT_LIMIT = None

DEFAULT_CYCLE = "-1" # -1 will return career totals.


class InfluenceExplorer(object):

    """
    Provides wrappers to the Influence Explorer APIs.

    Methods are divided into four categories. Entity methods can be accessed
    through the ``entities`` member, Politician methods through ``pol``, Individual
    methods through ``indiv`` and Organization through ``org``. For example::

        api = InfluenceExplorer(<your-key-here>)
        boehner_id = api.entities.search('john boehner')[1]['id]
        print api.pol.industries(boehner_id)
    """

    def __init__(self, api_key, base_url=DEFAULT_URL):
        """
        Create an API wrapper.

        API keys can be obtained from http://services.sunlightlabs.com.
        """

        self.base_url = base_url if base_url[-1] == '/' else base_url + '/'
        self.api_key = api_key
        self.entities = Entities(self)
        self.pol = Politician(self)
        self.indiv = Individual(self)
        self.org = Organization(self)
        self.map_ = Map(self)


    def _get_url_json(self, path, cycle=None, limit=None, **params):
        """ Low level call that just adds the API key, retrieves the URL and parses the JSON. """

        if cycle:
            params.update({'cycle': cycle})
        if limit:
            params.update({'limit': limit})

        params.update({'apikey': self.api_key})

        fp = urllib2.urlopen(self.base_url + path + '?' + urllib.urlencode(params))

        return json.loads(fp.read())


class SubAPI(object):
    def __init__(self, main_api):
        self._get_url_json = main_api._get_url_json


class Entities(SubAPI):
    """
    Methods related to searching, listing and ranking entities.

    Accessed as ``InfluenceExplorer.entities``.
    """

    def search(self, query):
        """
        Return entities with names matching the given query.

        Query terms are space separated. Matches must contain all terms
        from the query.
        """

        return self._get_url_json('entities.json', search=query.encode('ascii', 'ignore'))

    _camp_fin_markers = ['contributor_count', 'recipient_count', 'independent_expenditure_amount', 'fec_summary_count']
    _lobbying_markers = ['lobbying_count']
    _spending_markers = ['grant_count', 'loan_count', 'contract_count']
    _earmark_markers = ['earmark_count']
    _contractor_misconduct_markers = ['contractor_misconduct_count']
    _epa_echo_markers = ['epa_actions_count']
    _regulations_markers = ['regs_docket_count', 'regs_submitted_docket_count']
    _faca_markers = ['faca_committee_count', 'faca_member_count']

    def metadata(self, entity_id):

        """Return all available metadata for the given entity."""

        results = self._get_url_json('entities/%s.json' % entity_id)

        results['years'] = self._entity_years(results['totals'], self._camp_fin_markers + self._lobbying_markers + self._spending_markers)
        results['camp_fin_years'] = self._entity_years(results['totals'], self._camp_fin_markers)
        results['lobbying_years'] = self._entity_years(results['totals'], self._lobbying_markers)
        results['spending_years'] = self._entity_years(results['totals'], self._spending_markers)
        results['earmark_years'] = self._entity_years(results['totals'], self._earmark_markers)
        results['contractor_misconduct_years'] = self._entity_years(results['totals'], self._contractor_misconduct_markers)
        results['epa_echo_years'] = self._entity_years(results['totals'], self._epa_echo_markers)
        results['regulations_years'] = self._entity_years(results['totals'], self._regulations_markers)
        results['faca_years'] = self._entity_years(results['totals'], self._faca_markers)

        return results

    def _entity_years(self, totals, keys):
        years = [year for (year, values) in totals.items() if any([v for (k,v) in values.items() if k in keys]) and year != "-1"]
        years.sort()
        if years:
            return dict(start=years[0], end=years[-1])
        else:
            return {}

    def id_lookup(self, namespace, id):
        """
        Return the Influence Explorer entity ID based on a 3rd party ID.

        Valid namespaces include:

        * ``urn:crp:individual`` -- CRP's contributor or lobbyist ID
        * ``urn:crp:organization`` -- CRP's organization ID
        * ``urn:crp:recipient`` -- CRP's candidate ID
        * ``urn:crp:industry`` -- CRP's 3-letter category order
        * ``urn:crp:subindustry`` -- CRP's 5-letter category code
        * ``urn:nimsp:subindustry`` -- 5-letter category code added by NIMSP
        * ``urn:nimsp:organization`` -- NIMSP's organization ID
        * ``urn:nimsp:recipient`` -- NIMSP's candidate ID
        * ``urn:sunlight:lobbyist_registration_tracker_url`` -- URL of Sunlight's lobbyist registration tracker page
        """
        return self._get_url_json('entities/id_lookup.json', namespace=namespace, id=id)


    def count(self, type=None):
        """ Return the total count of entities. """
        params = {'count': 1}
        if type:
            params['type'] = type
        return int(self._get_url_json('entities/list.json', **params)['count'])


    def list(self, start, end, type=None):
        """ List all entities. """
        params = {'start': start, 'end': end}
        if type:
            params['type'] = type
        return self._get_url_json('entities/list.json', **params)


    # top n lists
    def top_n_individuals(self, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return the top individuals, by amount contributed. """
        return self._get_url_json('aggregates/indivs/top_%s.json' % limit, cycle)

    def top_n_indiv_democratic_donors(self, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return the top individuals, by amount contributed to Democrats. """
        return self._get_url_json('aggregates/indivs/party/D/top_%s.json' % limit, cycle)

    def top_n_indiv_republican_donors(self, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return the top individuals, by amount contributed to Republicans. """
        return self._get_url_json('aggregates/indivs/party/R/top_%s.json' % limit, cycle)

    def top_n_organizations(self, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return the top organizations, by amount contributed. """
        return self._get_url_json('aggregates/orgs/top_%s.json' % limit, cycle)

    def top_n_politicians(self, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT, office=None):
        """ Return the top politicians, by amount received. """
        if office in ('president', 'senate', 'house', 'governor'):
            return self._get_url_json('aggregates/pols/%s/top_%s.json' % (office, limit), cycle)

        return self._get_url_json('aggregates/pols/top_%s.json' % limit, cycle)

    def top_n_industries(self, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return the top industries, by amount contributed. """
        return self._get_url_json('aggregates/industries/top_%s.json' % limit, cycle)

    def candidates_by_location(self, location, cycle=DEFAULT_CYCLE):
        """ Internal use only. Not maintained. """
        return self._get_url_json('entities/race/%s.json' % location, cycle)

    def election_districts(self, cycle=DEFAULT_CYCLE):
        """ Internal use only. Not maintained. """
        return self._get_url_json('entities/race/districts.json', cycle)

    def bundles(self, entity_id, cycle=DEFAULT_CYCLE):
        """ Return any bundling data for the entity. """
        return self._get_url_json('aggregates/pol/{0}/bundles.json'.format(entity_id), cycle)

    def top_n_lobbyist_bundlers(self, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return top lobbyist bundlers. """
        return self._get_url_json('aggregates/indivs/lobbyist_bundlers/top_{0}.json'.format(limit), cycle)

    def top_n_orgs_lobbying(self, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT, is_industry=False):
        """ Return top industries by lobbying spending. """
        if is_industry:
            return self._get_url_json('aggregates/industries/lobbying/top_{0}.json'.format(limit), cycle)
        else:
            return self._get_url_json('aggregates/orgs/lobbying/top_{0}.json'.format(limit), cycle)

    def top_n_industry_donors_to_democrats(self, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return top industries by dollars donated to democrats. """
        return self._get_url_json('aggregates/industries/party/D/top_{0}.json'.format(limit), cycle)

    def top_n_industry_donors_to_republicans(self, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return top industries by dollars donated to republicans. """
        return self._get_url_json('aggregates/industries/party/R/top_{0}.json'.format(limit), cycle)

    def top_n_largest_donations_in_last_month(self, limit=DEFAULT_LIMIT):
        """ Return largest donations in last month. """
        return self._get_url_json('aggregates/fec/last_month/largest_{0}.json'.format(limit))

    def top_n_pacs_by_indexp(self, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return top PACs by independent expenditures. """
        return self._get_url_json('aggregates/orgs/indexp/top_{0}.json'.format(limit))

    def top_n_pols_by_indexp_by_office(self, office, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return top politicians by independent expenditures, by office. """
        if office in 'senate house president'.split():
            return self._get_url_json('aggregates/pols/indexp/{}/top_{}.json'.format(office, limit))

    def top_n_firms_by_income(self, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return top lobbying firms by income. """
        return self._get_url_json('aggregates/orgs/lobbying_firms/top_{0}.json'.format(limit))

    def top_n_indivs_by_area(self, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT, area=None):
        """ Return top individuals donating at the state level. """
        if area.lower() in ('state', 'federal'):
            return self._get_url_json('aggregates/indivs/{}/top_{}.json'.format(area, limit))

    def top_n_regs_submitters(self, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return top organizations submitting comments on regulations. """
        return self._get_url_json('aggregates/orgs/regulations/submitters/top_{}.json'.format(limit))

    def top_n_org_donors_by_area_contributor_type(self, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT, area=None, contributor_type=None):
        """ Return top organizations contributing via PACs or employees by area (state/federal). """
        if area in 'state federal'.split() and contributor_type in 'pac employee'.split():
            return self._get_url_json('aggregates/orgs/{}/{}/top_{}.json'.format(area, contributor_type, limit))



class Politician(SubAPI):
    """
    Methods relating to a politician entity.

    Accessed as ``InfluenceExplorer.pol``.
    """

    def contributors(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return the top organizational contributors. """
        return self._get_url_json('aggregates/pol/%s/contributors.json' % entity_id, cycle, limit)

    def sectors(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Not maintained. """
        return self._get_url_json('aggregates/pol/%s/contributors/sectors.json' % entity_id, cycle, limit)

    def industries(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return the top contributing industries. """
        return self._get_url_json('aggregates/pol/%s/contributors/industries.json' % entity_id, cycle, limit)

    def industries_unknown(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return the count and total from unknown industries """
        return self._get_url_json('aggregates/pol/%s/contributors/industries_unknown.json' % entity_id, cycle)

    def local_breakdown(self, entity_id, cycle=DEFAULT_CYCLE):
        """ Return the breakdown of in-state vs. out-of-state contributions. """
        return self._get_url_json('aggregates/pol/%s/contributors/local_breakdown.json' % entity_id, cycle)

    def contributor_type_breakdown(self, entity_id, cycle=DEFAULT_CYCLE):
        """ Return the breakdown of individual vs. organization contributions. """
        return self._get_url_json('aggregates/pol/%s/contributors/type_breakdown.json' % entity_id, cycle)

    def earmarks(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return top earmarks requested by this politician. """
        return self._get_url_json('aggregates/pol/%s/earmarks.json' % entity_id, cycle, limit)

    def earmarks_local_breakdown(self, entity_id, cycle=DEFAULT_CYCLE):
        """ Return breakdown of earmark amount for in-state vs. out-of-state projects. """
        return self._get_url_json('aggregates/pol/%s/earmarks/local_breakdown.json' % entity_id, cycle)

    def fec_summary(self, entity_id, cycle=DEFAULT_CYCLE):
        """ Return the latest figures from the FECs summary report. """
        return self._get_url_json('aggregates/pol/%s/fec_summary.json' % entity_id, cycle)

    def fec_timeline(self, entity_id, cycle=DEFAULT_CYCLE):
        """ Return weekly itemized fundraising totals for the candidate and opponents. """
        return self._get_url_json('aggregates/pol/%s/fec_timeline.json' % entity_id, cycle)

    def fec_indexp(self, entity_id, cycle=DEFAULT_CYCLE):
        """ Return independent expenditures for and against the candidate. """
        return self._get_url_json('aggregates/pol/%s/fec_indexp.json' % entity_id)


class Individual(SubAPI):
    """
    Methods relating to individual entities.

    Accessed as ``InfluenceExplorer.indiv``.
    """

    def org_recipients(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        ''' Return the top organizations receiving contributions. '''
        return self._get_url_json('aggregates/indiv/%s/recipient_orgs.json' % entity_id, cycle, limit)


    def pol_recipients(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        ''' Return the top politicians receiving contributions. '''
        return self._get_url_json('aggregates/indiv/%s/recipient_pols.json' % entity_id, cycle, limit)

    def party_breakdown(self, entity_id, cycle=DEFAULT_CYCLE):
        """ Return breakdown of amount contributed to each party. """
        return self._get_url_json('aggregates/indiv/%s/recipients/party_breakdown.json' % entity_id, cycle)

    def registrants(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """
        Return the lobbying firms that employed the individual.

        Only return data for individuals that are registered lobbyists.
        """

        return self._get_url_json('aggregates/indiv/%s/registrants.json' % entity_id, cycle, limit)

    def issues(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """
        Return the top issues the individual lobbied on.

        Only return data for individuals that are registered lobbyists.
        """
        return self._get_url_json('aggregates/indiv/%s/issues.json' % entity_id, cycle, limit)

    def clients(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """
        Return the clients the individual was contracted to work for.

        Only return data for individuals that are registered lobbyists.
        """
        return self._get_url_json('aggregates/indiv/%s/clients.json' % entity_id, cycle, limit)


class Organization(SubAPI):
    """
    Methods related to organization or industry entities.

    Accessed as ``InfluenceExplorer.org``.
    """

    def recipients(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return top politicians receiving contributions. """
        return self._get_url_json('aggregates/org/%s/recipients.json' % entity_id, cycle, limit)


    def pac_recipients(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        ''' Return the top organizations receiving contributions. '''
        return self._get_url_json('aggregates/org/%s/recipient_pacs.json' % entity_id, cycle, limit)

    def party_breakdown(self, entity_id, cycle=DEFAULT_CYCLE):
        """ Return breakdown of amount contributed to each party. """
        return self._get_url_json('aggregates/org/%s/recipients/party_breakdown.json' % entity_id, cycle)

    def level_breakdown(self, entity_id, cycle=DEFAULT_CYCLE):
        """ Return breakdown of amount contributed to state vs. federal races. """
        return self._get_url_json('aggregates/org/%s/recipients/level_breakdown.json' % entity_id, cycle)

    def registrants(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        '''
        Return lobbying firms hired.

        Only return data if organization is a client of lobbying firms.
        '''
        return self._get_url_json('aggregates/org/%s/registrants.json' % entity_id, cycle, limit)

    def issues(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """
        Return issues lobbied on.

        Only return data if organization is a client of lobbying firms.
        """
        return self._get_url_json('aggregates/org/%s/issues.json' % entity_id, cycle, limit)

    def bills(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """
        Return bills lobbied on.

        Only return data if organization is a client of lobbying firms.
        """
        return self._get_url_json('aggregates/org/%s/bills.json' % entity_id, cycle, limit)

    def lobbyists(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """
        Return lobbyists hired.

        Only return data if organization is a client of lobbying firms.
        """
        return self._get_url_json('aggregates/org/%s/lobbyists.json' % entity_id, cycle, limit)

    def registrant_clients(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """
        Return clients that hired this organization to lobby.

        Only return data if organization is a lobbying firm.
        """
        return self._get_url_json('aggregates/org/%s/registrant/clients.json' % entity_id, cycle, limit)

    def registrant_issues(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """
        Return issues this organization lobbied on.

        Only return data if organization is a lobbying firm.
        """
        return self._get_url_json('aggregates/org/%s/registrant/issues.json' % entity_id, cycle, limit)

    def registrant_bills(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """
        Return bill this organization lobbied on.

        Only return data if organization is a lobbying firm.
        """
        return self._get_url_json('aggregates/org/%s/registrant/bills.json' % entity_id, cycle, limit)


    def registrant_lobbyists(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """
        Return lobbyists employed.

        Only return data if organization is a lobbying firm.
        """
        return self._get_url_json('aggregates/org/%s/registrant/lobbyists.json' % entity_id, cycle, limit)

    def industry_orgs(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """
        Return top organizations within this industry.

        Only return data if entity is an industry.
        """
        return self._get_url_json('aggregates/industry/%s/orgs.json' % entity_id, cycle, limit)

    def fed_spending(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """
        Return top federal grants and contracts received.

        Matching is based on full-text search and may include incorrect matches
        or miss records. Not appropriate for automatic aggregation.
        """
        return self._get_url_json('aggregates/org/%s/fed_spending.json' % entity_id, cycle, limit)

    def earmarks(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return top earmarks received by organization. """
        return self._get_url_json('aggregates/org/%s/earmarks.json' % entity_id, cycle, limit)

    def contractor_misconduct(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return top misconduct instances by organization. """
        return self._get_url_json('aggregates/org/%s/contractor_misconduct.json' % entity_id, cycle, limit)

    def regulations_text(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return the regulatory dockets that most frequently mention this entity. """
        return self._get_url_json('aggregates/org/%s/regulations_text.json' % entity_id, cycle, limit)

    def regulations_submitter(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return the regulatory dockets with the most submissions from this entity. """
        return self._get_url_json('aggregates/org/%s/regulations_submitter.json' % entity_id, cycle, limit)

    def epa_echo(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return top EPA enforcement actions by organization. """
        return self._get_url_json('aggregates/org/%s/epa_enforcement_actions.json' % entity_id, cycle, limit)

    def faca(self, entity_id, cycle=DEFAULT_CYCLE, limit=DEFAULT_LIMIT):
        """ Return this entity's employees' memberships on federal advisory committees. """
        return self._get_url_json('aggregates/org/%s/faca.json' % entity_id, cycle, limit)

    def fec_summary(self, entity_id, cycle=DEFAULT_CYCLE):
        """ Return the latest figures from the FECs summary report. """
        return self._get_url_json('aggregates/org/%s/fec_summary.json' % entity_id, cycle)

    def fec_indexp(self, entity_id, cycle=DEFAULT_CYCLE):
        """ Return independent expenditures made by the committee. """
        return self._get_url_json('aggregates/org/%s/fec_indexp.json' % entity_id)

    def fec_top_contribs(self, entity_id, limit=DEFAULT_LIMIT):
        """ Return top contributors to the committee. """
        return self._get_url_json('aggregates/org/%s/fec_top_contribs.json' % entity_id)


class Map(SubAPI):
    """
    Methods that return geographical data.

    Accessed as ``InfluenceExplorer.org``.
    """
    def senate_independent_expenditures(self, cycle=DEFAULT_CYCLE):
        return self._get_url_json('aggregates/map/indexp/senate/lat_lng.geo.json', cycle)

    def house_independent_expenditures(self, cycle=DEFAULT_CYCLE):
        return self._get_url_json('aggregates/map/indexp/house/lat_lng.geo.json', cycle)

    def presidential_contribs(self, state, cycle=DEFAULT_CYCLE):
        return self._get_url_json('aggregates/map/contributions/presidential/{0}/lat_lng.geo.json'.format(state), cycle)
