import random
from fastapi.testclient import TestClient

# Import your FastAPI app instance from your main file
from app.main import app 
from app.core.security import get_admin_user
from app.models.core import Customer

# Initialize the test client
client = TestClient(app)

# ==========================================
# MOCK DEPENDENCY
# ==========================================
def override_get_admin_user():
    """Mocks an admin user so the test can pass the security gatekeeper."""
    return Customer(email="admin_tester@test.com", is_admin=True)

# Temporarily replace the real get_admin_user with our mock just for this test
app.dependency_overrides[get_admin_user] = override_get_admin_user


# ==========================================
# TESTS
# ==========================================
def test_phase4_routes():
    print("=== STARTING PHASE 4 VERIFICATION ===")
    
    # Test 1: Create a Plan (POST /plans/)
    random_id = random.randint(1000, 9999)
    plan_data = {
        "name": f"Automated Test Plan {random_id}",
        "price": 49.99,
        "feature_entitlements": ["api_access", "unlimited_storage"]
    }
    
    # Simulate a POST request to your endpoint
    response = client.post("/plans/", json=plan_data)
    
    if response.status_code == 201:
        print("✅ POST /plans/ : SUCCESS (Plan created in database!)")
        print(f"   -> Created: {response.json().get('name')} at ${response.json().get('price')}")
    else:
        print(f"❌ POST /plans/ : FAILED -> {response.status_code}")
        print(f"   -> Detail: {response.json()}")
        
    print("-" * 40)
    
    # Test 2: List Plans (GET /plans/)
    # Simulate a GET request to fetch all plans
    response_get = client.get("/plans/")
    
    if response_get.status_code == 200:
        plans = response_get.json()
        print("✅ GET /plans/  : SUCCESS (Fetched plans from database!)")
        print(f"   -> Total plans currently in database: {len(plans)}")
    else:
        print(f"❌ GET /plans/  : FAILED -> {response_get.status_code}")
        print(f"   -> Detail: {response_get.json()}")

    print("=====================================")

if __name__ == "__main__":
    test_phase4_routes()