from fastapi import HTTPException

# Updated import path to match app/core/security.py
from app.core.security import get_admin_user, create_access_token
from app.models.core import Customer

def test_security_and_rbac():
    print("=== STARTING PHASE 3 VERIFICATION ===")

    # 1. Create a dummy regular user
    regular_user = Customer(email="user@test.com", is_admin=False)
    
    # 2. Create a dummy admin user
    admin_user = Customer(email="admin@test.com", is_admin=True)

    # ---------------------------------------------------------
    # Test 1: Verify Token Generation
    # ---------------------------------------------------------
    try:
        token = create_access_token(data={"sub": admin_user.email})
        print(f"✅ Token Generation: SUCCESS")
        print(f"   -> Generated JWT: {token[:30]}... (truncated)")
    except Exception as e:
        print(f"❌ Token Generation: FAILED -> {e}")

    print("-" * 40)

    # ---------------------------------------------------------
    # Test 2: Verify Admin Access (Should Pass)
    # ---------------------------------------------------------
    try:
        # We manually pass the admin_user into the dependency
        get_admin_user(current_user=admin_user)
        print("✅ Admin Gatekeeper: SUCCESS (Admin was allowed through!)")
    except HTTPException:
        print("❌ Admin Gatekeeper: FAILED (Admin was blocked!)")

    print("-" * 40)

    # ---------------------------------------------------------
    # Test 3: Verify Regular User Access (Should be Blocked)
    # ---------------------------------------------------------
    try:
        get_admin_user(current_user=regular_user)
        print("❌ Regular User Gatekeeper: FAILED (Regular user slipped through!)")
    except HTTPException as e:
        if e.status_code == 403:
            print("✅ Regular User Gatekeeper: SUCCESS (User was properly blocked!)")
            print(f"   -> Block Reason: {e.detail}")
        else:
            print(f"❌ Regular User Gatekeeper: FAILED (Blocked, but wrong status code: {e.status_code})")

    print("=====================================")

if __name__ == "__main__":
    test_security_and_rbac()