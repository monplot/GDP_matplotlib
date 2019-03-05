# Import numpy as np
import matplotlib.pyplot as plt
import numpy as np
# Store pop as a numpy array: np_pop

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

life_exp=[43.8,71,80,32.5]
gdp_cap= [52,1550,5700,42.3]
np_pop=np.array(pop)

# Double np_pop
np_pop=np_pop*2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop, alpha=0.8, c= 'red' )

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call

plt.grid(True)


# Display the plot
plt.show()
