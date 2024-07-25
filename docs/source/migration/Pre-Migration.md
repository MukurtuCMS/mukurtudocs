# Pre-Migration Activities

We have built a pre-migration report that will identify all site content that needs to updated or modified before it can be migrated, and any content settings that will not be migrated. There are six categories included in the pre-migration report:

1) Text formats "Markdown" and "Display Suite code"
   - These formats are not supported by default in Mukurtu 4 and will not be migrated.
   - These formats are most commonly used to implement custom styling on basic pages, community pages, and in some DH items.
   - You will need to manually change these fields to use a supported format.
2) Content (nodes) with no assigned protocols
   - In Mukurtu 4 cultural protocols are required for ALL content types.
   - In Mukurtu 3 protocols were optional for dictionary words and collections, and were not included for person records and word lists.
   - You will most likely be able to use the bulk processing tool to add protocols to all content without one, but some content may require manual editing.
3) Media assets (atoms) with no assigned protocols
   - In Mukurtu 4 cultural protocols are required for ALL media assets.
   - In Mukurtu 3 protocols were optional, but recommended.
   - You will most likely be able to use the bulk processing tool to add protocols to all media assets without one, but some may require manual editing.
4) Dictionary words with additional media
   - In Mukurtu 4 there is both a thumbnail and an additional media field, and the additional media field works quite differently than in Mukurtu 3.
   - The contents of the additional media field will NOT be migrated.
   - You will need to manually move any media assets used in the Mukurtu 3 additional media field into the new thumbnail or additional media field if you want them to be included in the migration.
5) Dailymotion media assets (atoms)
   - Support for Dailymotion has been dropped in Mukurtu 4. We are not aware of any Mukurtu sites actively using Dailymotion.
   - Dailymotion media assets will NOT be migrated.
   - If you have any Dailymotion videos, you will need to move them to a different hosting platform and manually update the media assets and content that references them.
6) Scald authors field
   - The Scald "Authors" (scald_authors) field will not be migrated to Mukurtu 4. We are not aware of any Mukurtu sites actively using this field.
   - No action is required.

## Update Mukurtu 3

You will need to update your Mukurtu 3 site to the most current release (Version 3.XXX) to enable the new pre-migration tools. This process is the same as previous updates. 

If you are hosting with Reclaim Hosting, see these instructions to update your site: [Updating a Reclaim Hosted Mukurtu CMS Site](https://mukurtu.org/support/updating-a-reclaim-hosted-mukurtu-cms-site/)

## Run the pre-migration report

It is best for these actitivities to be run by a drupal administrator to ensure all content is addressed. The account *may* need to enrolled in additional protocols.

You can access the pre-migration report directly at /admin/reports/migration/summary (eg: https://mysite.com/admin/reports/migration/summary).

You can also access the report by following the "View Migration Preparation Summary" link on your dashboard.

![pre-migration01](../embeds/pre-migration01.png)

The report should run automatically, but you can click the "Run Pre-migration Report" button at any time to re-run the report. Your report will likely look something like this (but with more items identified).

![pre-migration02](../embeds/pre-migration02.png)

## Resolve pre-migration activities

Each category will have a summary in the "status" field on the right, which includes a link to a more detailed report and actions.

You MUST resolve "content nodes with no protocols" before resolving "media assets with no protocols". Otherwise ou can resolve these activities in whichever order your prefer.

### Content (nodes) with no assigned protocols

   - In Mukurtu 4 cultural protocols are required for ALL content types.
   - In Mukurtu 3 protocols were optional for dictionary words and collections, and were not included for person records and word lists.
   - You will most likely be able to use the bulk processing tool to add protocols to all content without one, but some content may require manual editing.

The content with missing cultural protocols report will allow you to filter, select, and apply bulk actions to update affected content.
![pre-migration-content-01](../embeds/pre-migration-content-01.png)

If necessary, filter by content type. This is useful if for example you know that all dicitonary words will continue to be public or under a single protocol, but collections will require a per-collection decision.
![pre-migration-content-02](../embeds/pre-migration-content-02.png)

If you need to review content one by one, you can click on the title to go to the content page.
If you want to bulk process content, from the operations dropdown select "set cultural protocols for content". All content selected will use the same protocol(s), so you may need to go through this multiple times selecting different content for different protocol(s).
![pre-migration-content-03](../embeds/pre-migration-content-03.png)

Select the content using the check boxes (you can select all content by using the checkbox in the top row).
Click "execute".
![pre-migration-content-04](../embeds/pre-migration-content-04.png)

Select the appropriate item sharing setting. If using one protocol, select "ALL" (the default setting when creating content).
![pre-migration-content-05](../embeds/pre-migration-content-05.png)

Use the checkboxes to select the appropriate protocol(s).
Click "next".
![pre-migration-content-06](../embeds/pre-migration-content-06.png)

If the list looks correct, click "confirm".
![pre-migration-content-07](../embeds/pre-migration-content-07.png)

A confirmation message will be displayed.
![pre-migration-content-08](../embeds/pre-migration-content-08.png)

### Media assets (atoms) with no assigned protocols

   - In Mukurtu 4 cultural protocols are required for ALL media assets.
   - In Mukurtu 3 protocols were optional, but recommended.
   - You will most likely be able to use the bulk processing tool to add protocols to all media assets without one, but some may require manual editing.

> SCREENSHOTS NEEDED

### Text formats "Markdown" and "Display Suite code"

> SCREENSHOTS NEEDED

### Dictionary words with additional media

   - In Mukurtu 4 there is both a thumbnail and an additional media field, and the additional media field works quite differently than in Mukurtu 3.
   - The contents of the additional media field will NOT be migrated.
   - You will need to manually move any media assets used in the Mukurtu 3 additional media field into the new thumbnail or additional media field if you want them to be included in the migration.

> SCREENSHOTS NEEDED

### Dailymotion media assets (atoms)

   - Dailymotion media assets will NOT be migrated.
   - There is no automated process to resolve Dailymotion videos.
   - If you have any Dailymotion videos, you will need to...
     1) Move them to a different hosting platform (either Vimeo or Youtube) or upload them directly to the site (not recommended).
     2) Create new media assets for the newly hosted videos.
     3) Replace the Dailymotion media assets with the new media assets in any DH items or other content where they are used.
     4) Delete the old Dailymotion media assets.

> SCREENSHOTS NEEDED

### Scald authors field

   - The Scald "Authors" (scald_authors) field will not be migrated to Mukurtu 4. There is a separate "author" field that automatically records the user responsible for uploading the media asset.
   - No action is required, you can leave this field populated and it will not affect the migration.

> SCREENSHOTS NEEDED


## Pre-migration work complete

When you are done running all the pre-migration activities, the report will indicate that...
- There are no nodes using these text formats.
- All content has cultural protocols
- All Scald Atoms have cultural protocols
- No dictionary words have additional media
- No Dailymotion atoms found
- No Scald Authors terms found

![pre-migration-complete](../embeds/pre-migration-complete.png)

> Please keep in mind that if you are continuing to work on the site before running the migration, you will need to ensure that new and update content will pass the pre-migration report (eg: when creating a new collection, ensure that it uses protocols). Shortly before beginning a migration, we STRONGLY recommend running a final pre-migration report and then placing the site in maintenance mode to prevent changes being made.
