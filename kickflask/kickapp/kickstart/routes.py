from flask import render_template, request
from kickstart import app

patterns = [
    # {"name": "Deploy a Web App", "category": "compute"},
    # {"name": "Deploy Azure SQL", "category": "databases"},
    # {"name": "Deploy Azure OpenAI", "category": "ai"},
    {
        "id": "entra-react",
        "name": "Secure React Login with Microsoft Entra External ID and Flask API", 
        "category": "compute",
        "description": (
            "Collect application identifiers for a react frontend"
            "and a Flask API using Microsoft Entra External ID."
        ),
        "tags": ["React", "Flask", "Microsoft Entra"],
        "icon": "",
        "fields": [
            ("tenent_id", "External Tenent ID"),
            ("frontend_client_id", "React Applications Client ID"),
        ],
    }
]
common_fields = [
    ("project_name", "Project Name"),
    ("subscription_id", "Azure Subscription ID"),
]

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    #Example: /home?category=compute sets category to "compute"
    category = request.args.get("category", "all")

    # All includes every patterns; other values filter by category.
    visible_patterns = [
        patterns
        for pattern in patterns
        if category == "all" or pattern["category"] == category
    ]
    pattern_id =  request.args.get("pattern")
    # Find the corresponding dictionary, or use none when none watches.
    selected_pattern = next(
        (pattern for pattern in patterns if pattern["id"] == pattern_id),
        None,
    )
    # An unknown pattern should not silently open the wrong form.
    if pattern_id and selected_pattern is None:
        abort(404)
    
    # Start with empty form values, validation errors, and confirmation.
    values = {}
    errors = []
    submitted = False

    # POST runs when the user presses "Review details"
    if requested.method == "POST":
        # Submitting requires a selected Patterns
        if selected_pattern is None:
            abort(400)
        # combine the shared inputs with this pattern's specific inputs.
        required_fields = common_fields + selected_pattern["fields"]
        
        # Read only the feilds defined by the server
        for field_name, label in required_fields:
            # Strip() removes accidental spaces at either end.
            values[field_name] = request.form.get(field_name, "").strip()
            # Validate required values in the server as well as in the HTML.
            if not values(field_name):
                errors.append(f"{label} is required.")
        # This confirms basic completeness, not azure deployment validity
        submitted = not errors


        
        
@app.route("/about")
def about():
    return render_template("about.html")
