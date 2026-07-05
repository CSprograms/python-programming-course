"""
NCERT Supplementary Program - Unit 10: Plotting Data using Matplotlib

Demonstration using the matplotlib.pyplot library

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
import matplotlib.pyplot as plt

days    = ['Monday','Tuesday','Wednesday',
           'Thursday','Friday','Saturday','Sunday']
tickets = [2000, 2800, 3000, 2500, 2300, 2500, 1000]

plt.plot(days, tickets, color='magenta', marker='o')
plt.title('Daily Ticket Sales')
plt.xlabel('Day')
plt.ylabel('Tickets Sold')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
