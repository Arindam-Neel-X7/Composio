"""Explicit researcher-selected URLs; no discovery or claim inference here."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCOPES = {
    2: 'HubSpot CRM APIs and remote CRM MCP; developer testing and authorized production tenants; current and explicitly labeled legacy auth; plan-specific capabilities not generalized',
    13: 'Freshdesk REST v2 and official MCP; verified agents and FDK apps; trial testing versus licensed production tenants; plan-specific capabilities not generalized',
    31: 'Google Ads API current Cloud-project access and OAuth; test accounts versus authorized production accounts; legacy developer-token documentation identified separately',
    58: 'Sherlock Project open-source username-search CLI; local installation for testing or deployment; third-party target-site access not guaranteed',
    91: 'NotebookLM assignment Enterprise API scope, now Gemini Notebook Enterprise; licensed user/project/IAM path for trial testing and paid production; personal MCP separately identified',
}
URLS = {
    2: [
        ('https://developers.hubspot.com/developer-platform-basics', 'official_product_page', ['testing','production']),
        ('https://developers.hubspot.com/docs/apps/developer-platform/build-apps/authentication/overview', 'primary_docs', ['testing','production']),
        ('https://developers.hubspot.com/docs/apps/legacy-apps/private-apps/overview', 'primary_docs', ['production']),
        ('https://developers.hubspot.com/docs/api-reference/latest/overview', 'primary_docs', []),
        ('https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server', 'primary_docs', ['testing','production']),
    ],
    13: [
        ('https://developers.freshdesk.com/api/', 'primary_docs', ['testing','production']),
        ('https://support.freshdesk.com/support/solutions/articles/215517-how-to-find-your-api-key', 'primary_docs', ['testing','production']),
        ('https://developers.freshworks.com/docs/app-sdk/v3.0/support_ticket/oauth-implementation-in-apps/', 'primary_docs', ['testing','production']),
        ('https://support.freshdesk.com/support/solutions/articles/50000011778', 'primary_docs', ['testing','production']),
        ('https://support.freshdesk.com/support/solutions/articles/50000012670', 'primary_docs', ['production']),
    ],
    31: [
        ('https://developers.google.com/google-ads/api/docs/oauth/overview', 'primary_docs', ['testing','production']),
        ('https://developers.google.com/google-ads/api/docs/api-policy/developer-token', 'primary_docs', ['testing','production']),
        ('https://developers.google.com/google-ads/api/docs/api-policy/access-levels', 'primary_docs', ['testing','production']),
        ('https://developers.google.com/google-ads/api/docs/best-practices/testing', 'primary_docs', ['testing','production']),
        ('https://developers.google.com/google-ads/api/docs/concepts/api-structure', 'primary_docs', []),
        ('https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server', 'primary_docs', ['testing','production']),
    ],
    58: [
        ('https://github.com/sherlock-project/sherlock', 'official_repository', []),
        ('https://sherlockproject.xyz/usage', 'primary_docs', []),
        ('https://raw.githubusercontent.com/sherlock-project/sherlock/master/LICENSE', 'official_repository', ['testing','production']),
    ],
    91: [
        ('https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks', 'primary_docs', ['testing','production']),
        ('https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks-sources', 'primary_docs', ['testing','production']),
        ('https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm', 'primary_docs', ['testing','production']),
        ('https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-licensing', 'primary_docs', ['testing','production']),
        ('https://github.com/Morfeu333/notebooklm-mcp', 'community_repository', []),
    ],
}

def main():
    sources = []
    for app, entries in URLS.items():
        for url, kind, envs in entries:
            sources.append(dict(app_id=app,url=url,kind=kind,scope=SCOPES[app],environments=envs,
                attribution_basis=('Repository publisher documents its own unofficial personal NotebookLM implementation; not Google endorsement' if kind == 'community_repository' else
                    'Sherlock assignment repository or project documentation linked from that repository' if app == 58 else
                    'Vendor-controlled developer/support documentation or official onboarding page; primary content read using web tool'),
                attribution_by='task04-research-agent-gpt-6.1-sol'))
    path = ROOT / 'sources.json'
    with path.open('x', encoding='utf-8') as f:
        json.dump({'sources':sources}, f, indent=2)
    assert len(sources) == 24 and {s['app_id'] for s in sources} == {2,13,31,58,91}
    print(path)

if __name__ == '__main__':
    main()
