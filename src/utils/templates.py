from box import Box

MAIN_APP_TEMPLATE = Box(
    {
        "html": {
            "sidebar_style": """
            <style>
            [data-testid="stSidebarNav"] ul {
              border: 2px solid #e1d4d4;
              box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.3);
              border-radius: 8px;
              padding: 1rem !important;
            }
            [data-testid="stSidebarNav"]li {
              margin-bottom: 0.5rem;
            }
            a {
              text-decoration: none !important;
              box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
              border-radius: 6px;
              padding: 0.5rem;
              gap: 1rem !important;
              transition: all 0.2s ease-in-out;
            }
            [data-testid="stSidebarNav"] span {
              font-size: 1.15rem !important;
              color: #ffffff !important;
            }
            :active, :hover {
              text-decoration: none !important;
            }
            [data-testid="stSidebar"] > div:first-child {
                background: linear-gradient(160deg, #5a60ff 0%, #7a5cff 100%);
                color: white;
                padding: 1rem;
            }
            [data-testid="stSidebar"][aria-expanded="true"] {
                width: 22rem !important;
            }
            img {
                border-radius: 12px;
                margin-bottom: 12px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.25);
                width: 80%;
            }
            button[kind="primary"] {
                background-color: #6C63FF !important;
                color: #ffffff !important;
                font-weight: 600 !important;
                border-radius: 10px !important;
                border: none !important;
                transition: all 0.25s ease-in-out;
            }
            </style>
            """,
            "footer": """
            <style>
            a:link, a:visited {
                text-decoration: underline;
                transition: all 0.3s ease;
            }

            a:hover, a:active {
                color: #ff4444;
                background-color: transparent;
                text-decoration: underline;
            }

            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-align: center;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 0.25rem 0;
                box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.15);
                border-top: 1px solid #ffffff20;
                backdrop-filter: blur(10px);
                z-index: 1000;
                height: 35px;
            }

            .footer p {
                margin: 0;
                font-size: 14px;
                font-weight: 500;
                text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
            }

            .footer a {
                color: #ffffff !important;
                font-weight: 600;
                text-decoration: none;
                border-bottom: 2px solid transparent;
                padding: 2px 4px;
                border-radius: 3px;
            }

            .footer a:hover {
                color: #ffeb3b !important;
                border-bottom: 2px solid #ffeb3b;
                background: rgba(255, 255, 255, 0.1);
            }
            </style>

            <div class="footer">
                <p>Developed with &nbsp; ❤ &nbsp; by
                <a href="https://www.recursivezero.com/" target="_blank">
                RecursiveZero</a></p>
            </div>
            """,
        },
    }
)
