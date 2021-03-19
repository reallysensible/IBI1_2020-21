gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
# A list of sorted values for the average exon length across all 10 genes
import numpy as np
a = np.array(gene_lengths)
b = np.array(exon_counts)
average_exon_length=(a/b).tolist()
average_exon_length.sort()
print(average_exon_length)


# A boxplot displaying the distribution of average exon length
import matplotlib.pyplot as plt
#change color and pattern
boxprops = dict(color  = 'teal',facecolor = 'paleturquoise', linewidth=2.5)
medianprops = dict(linestyle='-.', linewidth=2.5, color='teal')
capprops = dict(color = 'teal', linewidth=2.5)
whiskerprops = dict(color = 'teal', linewidth=2.5)
labels = ['exon'] #labels must be list
#plot
fig, ax = plt.subplots()
ax.boxplot(average_exon_length,
    patch_artist=True,
    boxprops = boxprops,
    medianprops = medianprops,
    capprops = capprops,
    whiskerprops = whiskerprops,
    labels = labels )
ax.set_title('Average Exon Length',fontsize=20)
# names for axes
for ax in [ax]:
    ax.set_ylabel('length distribution')

# horizontal grid
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

plt.show()
