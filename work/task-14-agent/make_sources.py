import json
from pathlib import Path
ROOT=Path('D:/Composio')
SCOPES={
71:'Notion hosted workspace REST API and official hosted MCP; internal connection and public OAuth integration paths; API version as documented, no dedicated sandbox assumed',
72:'Airtable hosted Web API and official hosted MCP; personal access token and OAuth paths; account plan and base permissions apply, no dedicated sandbox assumed',
73:'Linear hosted GraphQL API and official hosted MCP; personal API key and OAuth paths; workspace permissions apply, no dedicated sandbox assumed',
74:'Jira Cloud platform REST API v3 and Atlassian remote MCP; account API token and OAuth 2.0 3LO paths; excludes Jira Data Center and Server',
75:'Asana hosted REST API and official Asana V2 MCP; personal access token and OAuth paths; requested developer sandbox distinct from live workspace; Command MCP excluded',
76:'monday.com hosted platform GraphQL API v2 and official hosted MCP; personal V2 token and OAuth paths; free developer sandbox distinct from production workspace',
77:'ClickUp hosted public API v2 and official hosted MCP; personal API token and OAuth paths; excludes ClickUp consuming third-party MCP servers',
78:'Coda hosted REST API v1 and Coda hosted MCP; account API token paths; document permissions apply, no dedicated sandbox assumed',
79:'Smartsheet hosted REST API 2.0 and official hosted MCP; token and OAuth paths; Business/Enterprise API plan scope and requested developer environment distinct',
80:'Harvest time-tracking hosted API v2; personal access token and OAuth2 paths; excludes Greenhouse recruiting Harvest API and Forecast-only scope',
}
URLS={
71:['https://developers.notion.com/reference/intro','https://developers.notion.com/docs/authorization','https://developers.notion.com/docs/create-a-notion-integration','https://developers.notion.com/docs/mcp','https://developers.notion.com/docs/get-started-with-mcp'],
72:['https://airtable.com/developers/web/api/introduction','https://support.airtable.com/docs/creating-personal-access-tokens','https://support.airtable.com/docs/airtable-api-faqs','https://support.airtable.com/docs/using-the-airtable-mcp-server','https://airtable.com/developers/web/api/oauth-reference'],
73:['https://linear.app/developers/graphql','https://linear.app/developers/oauth-2-0-authentication','https://linear.app/docs/mcp','https://linear.app/docs/api-and-webhooks'],
74:['https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/','https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/','https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/','https://atlassian.github.io/atlassian-mcp-server/','https://developer.atlassian.com/cloud/jira/platform/getting-started/'],
75:['https://developers.asana.com/docs/overview','https://developers.asana.com/docs/personal-access-token','https://developers.asana.com/docs/oauth','https://developers.asana.com/docs/developer-sandbox','https://developers.asana.com/docs/integrating-with-asanas-mcp-server','https://developers.asana.com/reference/gettasks'],
76:['https://developer.monday.com/api-reference/docs/introduction-to-graphql','https://developer.monday.com/api-reference/docs/authentication','https://developer.monday.com/api-reference/docs/developer-sandbox','https://developer.monday.com/apps/docs/oauth','https://developer.monday.com/api-reference/docs/mcp-api-token','https://support.monday.com/hc/en-us/articles/28588158981266-Get-started-with-monday-MCP'],
77:['https://developer.clickup.com/docs/general','https://developer.clickup.com/docs/authentication','https://developer.clickup.com/docs/mcp-server','https://developer.clickup.com/docs/mcp-tools','https://developer.clickup.com/reference/gettasks'],
78:['https://coda.io/developers/apis/v1','https://help.coda.io/hc/en-us/articles/39555814921229-Coda-API','https://help.coda.io/hc/en-us/articles/44722661982989-Connect-to-the-Coda-MCP'],
79:['https://developers.smartsheet.com/api/smartsheet/introduction','https://developers.smartsheet.com/api/smartsheet/guides/basics/authentication','https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth','https://developers.smartsheet.com/ai-mcp/smartsheet/mcp-server-tools','https://www.smartsheet.com/content-center/best-practices/tips-tricks/api-getting-started','https://help.smartsheet.com/articles/2483656-install-smartsheet-connector-claude'],
80:['https://help.getharvest.com/api-v2/','https://help.getharvest.com/api-v2/introduction/overview/general/','https://help.getharvest.com/api-v2/authentication-api/authentication/authentication/','https://www.getharvest.com/pricing','https://help.getharvest.com/api-v2/time-tracking-api/time-entries/time-entries/'],
}
def main():
 d=ROOT/'work/task-14-agent'; d.mkdir(exist_ok=True)
 sources=[]
 for app,urls in URLS.items():
  for u in urls:
   kind='official_product_page' if '/pricing' in u or '/content-center/' in u else 'primary_docs'
   sources.append(dict(app_id=app,url=u,kind=kind,scope=SCOPES[app],environments=['testing','production'],attribution_basis='Researcher selected vendor-controlled developer or support documentation; attribution requires independent review',attribution_by='task14-codex-research-worker'))
 (d/'sources-001.json').write_text(json.dumps({'sources':sources},indent=2),encoding='utf-8')
if __name__=='__main__':main()
