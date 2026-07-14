# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/views/main.scala.html

- repository: `SysML-v2-API-Services`
- source_path: `app/views/main.scala.html`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/views/main.scala.html
- source_bytes: 924
- source_sha256: `02de82d5af75d1514055a7a95bbdb731d7654209759ad45e665c287b18d7fd1a`
- decoded_as: `utf-8`


## EXACT SOURCE

````html
@*
 * This template is called from the `index` template. This template
 * handles the rendering of the page header and body tags. It takes
 * two arguments, a `String` for the title of the page and an `Html`
 * object to insert into the body of the page.
 *@
@(title: String)(content: Html)

<!DOCTYPE html>
<html lang="en">
    <head>
        @* Here's where we render the page title `String`. *@
        <title>@title</title>
        <link rel="stylesheet" media="screen" href="@routes.Assets.versioned("stylesheets/main.css")">
        <link rel="shortcut icon" type="image/png" href="@routes.Assets.versioned("images/favicon.png")">
    </head>
    <body>
        @* And here's where we render the `Html` object containing
         * the page content. *@
        @content

        <script src="@routes.Assets.versioned("javascripts/main.js")" type="text/javascript"></script>
    </body>
</html>

````
