"""
    Provided Themes:
        Alpine
            - ag-theme-alpine
            - ag-theme-alpine-dark
        
        Balham
            - ag-theme-balham
            - ag-theme-balham-dark
            - Themes for professional data-heavy applications

        Material
            - ag-theme-material

        Bootstrap
            - ag-bootstrap

        All the themes are loaded for you by the dash-ag-grid component. To use a theme, add the theme to the className prop
        default is className="ag-theme-alpine"
        if you add other class names, it's necessary to include the theme, even when you use the default theme. 

    Loading CSS files:
        Dash loads the stylesheets in a certain way. Here's the order:

            1 - Files included as external stylesheets in the app constructor app=Dash(__name__, external_stylesheets=[])

            2 - .css files in the /assets folder, in alphanumerical order by filename

            3 - The grid's stylesheets when you import dash_ag_grid


    Customizing the theme: 
        
        Global changes:
            Note that it's necessary to use !important because the .css files in the /assets folder are loaded before the grid's theme.

        Creating a class to use with a theme: 
            The grid wrapper element should specify both the class name of the theme you're modifying, and the name of the custom theme.

            .css file
            .ag-theme-alpine.ag-theme-acmecorp {
                --ag-odd-row-background-color: #aaa;
            }
            in table definition
            className="ag-theme-alpine ag-theme-acmecorp"

        Creating your own theme (from scratch)

    """
