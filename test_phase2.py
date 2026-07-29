from pydantic import ValidationError

# Updated path to match app/schemas/customer.py
from app.schemas.customer import PlanCreate, PlanUpdate

def test_pydantic_schemas():
    print("=== STARTING PHASE 2 VERIFICATION ===")

    # Test 1: Passing Valid Data
    try:
        valid_plan = PlanCreate(
            name="Pro Tier",
            price=29.99,
            feature_entitlements=["priority_support", "unlimited_users"]
        )
        print("✅ Valid Data Test: SUCCESS")
        print(f"   -> Plan Name: {valid_plan.name}")
        print(f"   -> Price: ${valid_plan.price}")
        print(f"   -> Default Currency applied: {valid_plan.currency}")
        print(f"   -> Default Status applied: {valid_plan.status}")
    except ValidationError as e:
        print("❌ Valid Data Test: FAILED")
        print(e)

    print("-" * 40)

    # Test 2: Passing Invalid Data (Missing the required 'price' field)
    try:
        invalid_plan = PlanCreate(
            name="Starter Tier",
            description="A plan with no price should fail validation."
        )
        print("❌ Invalid Data Test: FAILED (Pydantic accepted bad data!)")
    except ValidationError as e:
        print("✅ Invalid Data Test: SUCCESS (Pydantic blocked the bad data!)")
        print(f"   -> Block Reason: {e.errors()[0]['msg']}")

    print("=====================================")

if __name__ == "__main__":
    test_pydantic_schemas()