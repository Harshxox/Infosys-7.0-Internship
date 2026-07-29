from app.database.connection import SessionLocal
from app.models.core import Customer, Plan

def verify_database():
    db = SessionLocal()
    
    print("=== STARTING PHASE 1 VERIFICATION ===")
    
    # 1. Check the Admin Account
    admin = db.query(Customer).filter(Customer.email == "harshdeep@admin.com").first()
    if admin:
        print(f"✅ Master Admin Check: SUCCESS")
        print(f"   -> Email: {admin.email}")
        print(f"   -> is_admin status: {admin.is_admin}")
    else:
        print("❌ Master Admin Check: FAILED (Account not found)")

    # 2. Check the Plan Table
    try:
        # We just try to count the plans. If the table doesn't exist, this will crash.
        plan_count = db.query(Plan).count()
        print(f"✅ Plan Table Check: SUCCESS")
        print(f"   -> The table exists and currently has {plan_count} plans inside.")
    except Exception as e:
        print("❌ Plan Table Check: FAILED")
        print(f"   -> Error: The table might not be created in PostgreSQL yet. Did you run your migrations?")
        print(f"   -> Details: {e}")
        
    print("=====================================")
    db.close()

if __name__ == "__main__":
    verify_database()