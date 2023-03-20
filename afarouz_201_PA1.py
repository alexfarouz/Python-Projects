#-------------------------------------------------------------------------------
#Name: George Mason
#Assignment: PA 1
#Due Date: 12/31/1999
#-------------------------------------------------------------------------------
#Honor Code Statement: I received no assistance on this assignment that
#violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
#Comments and Assumptions: A note to the grader as to any problems or
#uncompleted aspects of the assignment, as well as any assumptions about the #
#meaning of the specification. You can write in N/A if you don’t have any
#comments/assumptions.
#-------------------------------------------------------------------------------
#NOTE: width of source code should be <=80 characters to be readable on-screen.
#12345678901234567890123456789012345678901234567890123456789012345678901234567890
#10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

#step 1: prints the required phrase
print("Pet Love Vet Weekly Profit Calculator")

#step 2: asks for inputs from all the users
total_patients = int(input("Total patients this week: "))
total_per_patient = float(input("Total charged per patient: "))
hourly_pay = float(input("Part timer's hourly pay: "))
part_timers = int(input("Number of part-timers: "))
total_hours_worked = float(input("Part-timers total hours worked: "))
supply_costs = float(input("Total supply costs: "))
overhead_fees = float(input("Overhead fees: "))

#step 3: finds total revenue called gross_made
gross_made = (total_patients * total_per_patient)

#step 4: finds total_paid_to_part_timers (without OT, see below)
total_paid_to_part_timers = (hourly_pay * total_hours_worked)

#step 5: calculates the taxes paid
tax_paid = (gross_made * 0.15)

'''
step 6:
the variable 'losses' calculates all the money spent in total (without OT,
see below). In net_profit, 'losses' is subtracted from gross_made.
'''
losses = (total_paid_to_part_timers + tax_paid + supply_costs + overhead_fees)
net_profit = (gross_made - losses)

'''
the following lines of code calculate OT:
non_ot_hours calculates the amount of hours worked without OT. Subrtracting
this value from total_hours_worked gives the amount of OT hours.
With the OT hours, you multiply it by hourly_pay and then 1.5 to account for
OT. I then added ot_pay to non_ot_hours * hourly_pay to create the variable
labor.To find out the new profit after OT, I made a variable called
new_losses in which I subtracted the original total_paid_to_part_timers
from the variable losses because total_paid_to_part_timers takes the value
of hourly_pay and multiplies it by total_hours_worked, without accounting
for OT. Now wages are out of the new_losses variable, we can implement a
new value which accounts for OT. I added the labor variable from earlier
to new_losses. Now, net_profit is calculated with OT!
'''
non_ot_hours = float(part_timers * 20)
ot_hours = float(total_hours_worked - non_ot_hours)
ot_pay = float(ot_hours * hourly_pay * 1.5)
labor = (non_ot_hours * hourly_pay) + ot_pay
new_losses = losses - total_paid_to_part_timers
new_losses += labor
net_profit = float(gross_made - new_losses)

#step 7: outputs all the required results rounded to 2 decimal places
print()
print("Gross Made:" + "\t" + str(round(gross_made, 2)))
print("Total paid to Part-Timers:" + "\t" + str(round(labor, 2)))
print("Total tax paid:" + "\t" + str(round(tax_paid, 2)))
print("Net Profit for the Week:" + "\t" + str(round(net_profit, 2)))
