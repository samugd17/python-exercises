def run(age: int, weight: int, heartbeat: int, platelets: int) -> bool:
    # TODO
    
    suitable_for_donation = False
    if 18 <= age <= 65:
        if weight >= 50:
            if 50 <= heartbeat <= 110:
                if platelets >= 150000:
                    suitable_for_donation = True

    return suitable_for_donation


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
