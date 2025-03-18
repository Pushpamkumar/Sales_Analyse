# Create all database tables
with app.app_context():
    # Import models here to avoid circular imports
    from models import User, Lead
    from models import User, Lead, CustomReport, LeadActivity
    db.create_all()
@login_manager.user_loader