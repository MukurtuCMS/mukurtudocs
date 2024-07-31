# Can the system administrator view all content?

Data, media, and content privacy is incredibly important. It is a complex subject, but for the focus of this FAQ, there are two areas to consider:
1) Access to content within the site by users and visitors.
2) Access to content through the server or hosting environment itself.

## Access to content within the site

For all authenticated site users and visitors access to content is fully controlled by the sites cultural protocols. Please refer to the documentation on cultural protocols and user roles for more detail. The only exception to this are users with the role "drupal administrator".  This role is typically only given to one or two users per site and is a necessary role for at least one user to have on a respective Mukurtu site.

Users with the "drupal administrator" role *do* bypasses cultural protocols when using the site and can access all site content, media, etc.
- This is effectively unavoidable due to the nature of the technologies used.
- Thiat said, it is also necessary for someone to have this kind of access. When doing certain troubleshooting and maintenance tasks, it is necessary to have access to both system tools and content access permissions which most user accounts wouldn't have.
- Additionally, a user with this role serves as a backup if a community manager or protocol steward leaves the project or locks themselves out of their account (assuming there are no other users who are active managers or stewards within their communities and protocols). Someone else needs to be able to access and manage those groups - either to restore access or assign new managers and stewards.
- This is one of the reasons that we strongly recommend using a "Mukurtu administrator" account for most day-to-day work, and reserving the drupal admin account for troubleshooting, maintenance, etc, which can be done with a "drupal administrator" account as needed.
- By default, the usaer account that is created at the time the site is installed will have the "drupal administrator" role. Other users would have to be manually assigned this role.

## Access to content through the server or hosting environment

Someone with access to the server or hosting environment directly would also have access to the contents of the database (media, content, etc).
- Similar to the notes above, that is simply the nature of this kind of technology. In order to properly implement and maintain complex systems like this, a server/system administrator will have root level access.
- This is a clear reason why it's important to work with a trsuted IT department or third party vendor for hosting. On a technical level they should be managing security on their systems to ensure that no unwanted person can access the databases. On a policy level you should ensure that your agreements and contracts require your hosting provider to respect your expectations and needs for access and control.

> The Mukurtu team does not have any awareness of, or access to your Mukurtu site. Every site is independently installed and managed; we do NOT have any kind of remote or backdoor access to any Mukurtu site. The only exception is if our team is hosting your site on contract, if which case we are acting as your system/server administrator and drupal administrator.
