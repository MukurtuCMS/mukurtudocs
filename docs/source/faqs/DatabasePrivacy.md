# Can the system administrator view all content?

Data, media, and content privacy is incredibly important. 


There are two areas to consider:
1) Access to content within the site by users and visitors.
2) Access to content through the server or hosting environment itself.


## Access to content within the site

WITHIN the site, the drupal administrator role does have the ability to bypass protocols to access content.
This is partially unavoidable because of the way Drupal works, but we could in theory explore locking it down further.
This is also important/necessary though. What would happen if a there was a single community manager/protocol steward and they left the project or locked themselves out of their account? Someone needs to be able to access that stuff and manage access in a worst case scenario. Ditto for other technical troubleshooting – sometimes you need a combination of access AND system permissions that most users won’t have to resolve issues.
This is one of the reasons that we recommend using a separate Mukurtu administrator account for most day-to-day work, and reserving the drupal admin account for troubleshooting, maintenance, etc.

## Access to content through the server or hosting environment

On the SERVER side, yes the server/system administrator would be able to access the contents of the database.
That’s again kind of how servers work, and there is an expectation that whomever is doing that server maintenance IS building in the appropriate security tools (that’s all outside the control of Mukurtu), and it’s important to use a trusted vendor who will respect community needs.
I truly don’t think there is a way to build a database/platform/etc where a system administrator *cannot* access the database…
