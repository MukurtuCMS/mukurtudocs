# 3) Mukurtu 3 Pre-Migration Activities

The pre-migration report will identify all site content that needs to be updated or modified before it can be migrated to Mukurtu 4. The report will also identify any content settings that will not be migrated. 

> The pre-migration report only addresses stock Mukurtu content and features. For example, if you have created a new content type, or added a new field, it will not be reflected in this report. Please contact [support@mukurtu.org](mailto:support@mukurtu.org) with any questions.

There are six categories included in the pre-migration report:

1) Content (nodes) with no assigned protocols
2) Media assets (atoms) with no assigned protocols
3) Text formats: "Markdown" and "Display Suite code"
4) Dictionary words with additional media
5) Dailymotion media assets (atoms)
6) Scald authors field

## Run the pre-migration report and clear caches

It is best for these actitivities to be run by a Drupal administrator to ensure all content is addressed. Depending on how you have assigned protocol membership, the account may need to be enrolled in additional protocols to apply protocols to content and media.

You can access the pre-migration report directly at /admin/reports/migration/summary (eg: https://mysite.com/admin/reports/migration/summary).

You can also access the report by following the "View Migration Preparation Summary" link on your dashboard.

![pre-migration01](../embeds/pre-migration01.png)

The report should run automatically, but you may need to click the "Run Pre-migration Report" button run the report. 

![pre-migration02](../embeds/pre-migration02.png)

After running the pre-migration report, clear all site caches to ensure the report summary is updated. 
Hover over the home icon at the top left of the page, and click "Flush all caches". The page will reload when complete, which may take some time depending on the size of the site and server configuration.

![pre-migration-cache-clear](../embeds/pre-migration-cache-clear.png)

The report should automatically update as you complete the activities below. If the report summary does not automatically update, re-run the report and clear caches as shown above.

## Resolve pre-migration activities

Each category will have a summary in the "status" field on the right, which includes a link to a more detailed report and actions.

You should resolve "content nodes with no protocols" and "dictionary words with additional media" before resolving "media assets with no protocols" to avoid going through some steps multiple times (there is no harm in this, it just requires repeating steps). Otherwise ou can resolve these activities in whichever order your prefer.

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

The Scald Atoms with missing cultural protocols report will allow you to filter, select, and apply bulk actions to update affected media assets.
If you have media assets that already had a protocol assigned during their creation, they will not be listed here.

![pre-migration-media-01](../embeds/pre-migration-media-01.png)

If necessary, filter by media type.

![pre-migration-media-02](../embeds/pre-migration-media-02.png)

If you need to review media assets one by one, you can click on the title to go to the media asset page.
If you want to bulk process media, from the operations dropdown select one of the two actions:
- "Duplicate cultural protocols from item"
  - This is going to be the most commonly used action.
  - It will look at the protocol(s) used on the content and apply those same protocols to the media assets.
  - This will mostly apply in cases where for public content users didn't bother applying protocols to media assets, or where for non public content protocols were missed on media assets.
- "Set cultural protocols for scald atoms".
  - On many sites this action may not be needed at all.
  - It allows you to manually set protocols on media assets and works the same as "Content (nodes) with no assigned protocols" - see above for instructions.
  - This will be used if there are media assets that are NOT included in any content. In this case you may instead prefer to delete unused media assets, or create a "to be reviewed" protocol to ensure that the migration can be complete and you can review them later.
  - It can also be used in cases where you want a different protocol between content and media assets, but it is likely that you have already implemented that, since it's usually the case where media assets will have a stricter protocol than the content.

Some media assets may require manually assigning a protocol. Likely cases include:
- Where a media asset has been used in multiple content (eg: in a DH item and set as a collection image)

Select the media assets using the check boxes (you can select all content by using the checkbox in the top row).
Click "execute".

![pre-migration-media-03](../embeds/pre-migration-media-03.png)

If the list looks correct, click "confirm".

![pre-migration-media-04](../embeds/pre-migration-media-04.png)

A confirmation message will be displayed.

![pre-migration-media-05](../embeds/pre-migration-media-05.png)


### Text formats "Markdown" and "Display Suite code"

- In Mukurtu 4 the "markdown" and "display suite code" formats are no longer supported in the default HTML field editor. Plain text, basic HTML, and Full HTML are still supported.
- These formats are most commonly used to implement custom styling on basic pages, community pages, and in some DH items.
- This setting will need to manually changed on all field that use one of these formats.
- If you have used either format to achieve specific styling, it may be replicable with one of the HTML settings in Mukurtu 4. We recommend taking screenshots of the pages and copying the code you wrote so that it can be reviewed and re-implemented after migration.
- This may affect any kind of site node, eg: basic pages, community pages, protocol pages, DH items (Traditional Knowledge, Cultural Narrative, Description fields), Collection (Description field).


From the Text formats Markdown and Display Suite code report page, one-by-one, click on the title of the content to be edited.
> TEXT FORMAT SUMMARY NEEDS TO BE ADDED, SCREEENSHOT NEEDED

For a page, click "page menu" and "edit".

![pre-migration-text-01](../embeds/pre-migration-text-00.png)

For content, click "item menu" and "edit".

![pre-migration-text-01](../embeds/pre-migration-text-00a.png)

Located the affected HTML field(s). They will list "Display suite code" or "markdown" in the dropdown menu below the text box.

![pre-migration-text-01](../embeds/pre-migration-text-01.png)

Change the setting to "plain text", "filtered HTML", or "full html" as needed. Save the page or content (not shown).

![pre-migration-text-02](../embeds/pre-migration-text-02.png)


### Dictionary words with additional media
> NEED BETTER SCREENSHOTS

   - In Mukurtu 4 the single HTML "additional media" field has been replaced by two new fields: thumbnail (image only) and media assets (all media types, the same as the digital heritage item media assets field.) 
   - The contents of the additional media field will NOT be migrated.
   - You will need to manually move any media assets used in the Mukurtu 3 additional media field into the new thumbnail or media assets field if you want them to be included in the migration.
   - This can also be accomplished with regular batch update tools if preferred.

From the Dictionary words with additional media report, click on the dictionary word to be edited.

![pre-migration-dictionary-media-01](../embeds/pre-migration-dictionary-media-01.png)

From the "item menu" at the lef tof the page, select "edit". 

If necessary, inspect the embedded media asset to find its name. Locate the media asset(s) in the media library, and drag and drop them into the new "additional media addets" field.

![pre-migration-dictionary-media-02](../embeds/pre-migration-dictionary-media-02.png)

Ensure that the new field is showing the media assets, then delete the contents of the old "additional media" field.

![pre-migration-dictionary-media-03](../embeds/pre-migration-dictionary-media-03.png)

Save the item (not shown).

### Dailymotion media assets (atoms)

   - Support for Dailymotion has been dropped in Mukurtu 4. We are not aware of any Mukurtu sites actively using Dailymotion.
   - Dailymotion media assets will NOT be migrated.
   - There is no automated process to resolve Dailymotion videos.
   - If you have any Dailymotion videos, you will need to...
     1) Move them to a different hosting platform (either Vimeo or Youtube) or upload them directly to the site (not recommended).
     2) Create new media assets for the newly hosted videos.
     3) Replace the Dailymotion media assets with the new media assets in any DH items or other content where they are used.
     4) Delete the old Dailymotion media assets.


> SCREENSHOTS NEEDED?

### Scald authors field

   - The Scald "Authors" (scald_authors) field will not be migrated to Mukurtu 4. There is a separate "author" field that automatically records the user responsible for uploading the media asset.
   - No action is required, you can leave this field populated and it will not affect the migration.
   - If you do choose to resolve these messages follow the steps below. This can also be accomplished with regular batch update tools if preferred.

From the Scald Authors report, click on the title of the media asset to be edited.

![pre-migration-scald-authors-01](../embeds/pre-migration-scald-authors-01.png)

From the "page menu" select "edit".

![pre-migration-scald-authors-02](../embeds/pre-migration-scald-authors-02.png)

Expand the "additional fields" section.

![pre-migration-scald-authors-03](../embeds/pre-migration-scald-authors-03.png)

Locate the "authors" field and delete any terms. If you need to preserve these terms, consider entering them in the "people" or "contributor" field, as appropriate.

![pre-migration-scald-authors-04](../embeds/pre-migration-scald-authors-04.png)

With the field empty, click "Finish".

![pre-migration-scald-authors-05](../embeds/pre-migration-scald-authors-05.png)

A confirmation message will be displayed.

![pre-migration-scald-authors-06](../embeds/pre-migration-scald-authors-06.png)


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
