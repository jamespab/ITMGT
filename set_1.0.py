def savings(gross_pay, tax_rate, expenses):
    applied_tax = gross_pay * (1-tax_rate)
    savings= int(applied_tax - expenses)
    return savings


    def material_waste(total_material, material_units, num_jobs, job_consumption):
        consumption= num_jobs*job_consumption
        material_remainder = str(total_material - consumption) + material_units
        return(material_remainder)
    

    def interest(principal, rate, periods):
        interest_rate = rate*periods
        simple_interest = principal * interest_rate
        pre_final_value= int(principal +simple_interest)
        final_value = math.floor(pre_final_value)
        return (final_value)