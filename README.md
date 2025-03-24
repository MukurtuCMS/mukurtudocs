# Mukurtu 4 User Manual

> much of this is copied from the Omeka Classic documentation purely as an example and needs to be rewritten!

[Mukurtu CMS](https://mukurtu.org) is a......

The codebase is available in the [Mukurtu 4 GitHub repository](https://github.com/MukurtuCMS/Mukurtu-CMS).

This repository is the content of the [Mukurtu 4 User Manual](https://mukurtudocs.readthedocs.io/en/latest/index.html) and is best viewed on the official site.

## Contributing to the User Manual

If you notice something that could be improved, we would love your help. 

- This is documentation for ordinary users, not developers. Please use clear, jargon-free language. 
- Explain every possible step, even the ones which seem obvious. It is better for users to skip a step they've already completed than be confused by a leap they can't follow. Do not assume any prior knowledge of technology on the part of the user for this documentation.
- Break longer tasks up into short paragraphs or lists.
- Use illustrative images when needed, especially to indicate which button or link users should engage with.

If you are cloning the user manuals to your local computer and creating a branch, you may wish to [install and use MkDocs](https://www.mkdocs.org/#installation) to preview your changes and ensure the formatting and syntax are correct.

## Publishing to Read the Docs
- Edit in GitHub (browser)
- Use GitHub Desktop
- Use Visual Studio Code

**In Github Desktop**
1. Fetch origin (to work on the most up to date version)
2. Create a new branch
3. Open in VS Code
4. Make your changes
5. When ready, publish branch (may be superseded by committing)
6. When ready, commit changes to branch
7. Push origin
8. When ready, create pull request, you will be taken to browser
   - If more work 
9. Assign a reviewer if needed
10. Either create PR for review or draft PR if more work is needed


## Formatting 

**Topics**

**New articles**

**Article titles** must use H1 (`#`)

**Section headings** should start with H2 (`##`) and go down to H4. Create sections where it is logical in the documentation structure; they will appear in the left navigation of the documentation. Use "Sentence case for section headings", not "Camel Case".
  
**Links** should be composed as relative to the current file. They will look something like `../Plugins/CSV_Import.md` if you are linking to a page that sits within a folder, or `../Admin/Users.md#add-a-user` if you are linking to a section of a page. Do not forget the `.md` part of the page.
 
Links to external websites require the full URL as well as the addition of "{target=_blank}" after the link syntax: for example, `[create a new issue](https://github.com/omeka/classic-enduser/issues){target=_blank}`.

**Images** for a page go into the `embed` directory. Name images clearly, starting with an indicator of the relevant page, and use an underscore to separate out the image's purpose (for example, `items_addItem.png`).

Images should never give information that is not provided in the text (or in the image alt text and title). No one with vision problems should be missing out. Think of images as a shortcut, not the only route, to understanding how to do something. 

All images should have alt text. A title can also be supplied if having some pop-up text would be useful to readers. An image entered in Markdown looks like this:

```
Some text ends here.

![Alt text for the image goes here.](../doc_files/animage_pathGoesHere.png "An optional title which will appear when a user mouses over the image.")

More text picks up here.
```

The maximum display width of an image in the user manuals currently is around 1300px (actually 1296px). A screenshot of the full Omeka Classic interface (public or admin side) should be large. Images can be saved larger (up to 2000px wide) so that readers can open them in new tabs and inspect them in full-scale detail if desired. 

A screenshot of a portion of the interface, such as the left-hand navigation, should appear at full scale for maximum readability. Currently, Omeka Classic has a left-side menu-bar width of about 200px, and a main content width of about 1040px, on a 1920x1080 screen. Expand the browser window wide enough to add some whitespace and keep things from looking cramped, but screenshots do not need to be the full width of your monitor.

**Format your text** as follows: 

Buttons appear in quotes, as in the "Save" button. 

You can highlight interface features (such as page titles, page tabs, links, dropdown menus, and checkboxes) in **bold**. 

URLs, file paths, bits of code, and metadata fields are highlighted using `code formatting`. 

## Rights

This documentation is [CC-BY-NC](https://creativecommons.org/licenses/by-nc/4.0/).
