def data_distribution(data , n_bins):
    """ Draws a chart showing data distribution
        by combining an histogram and a boxplot

    Parameters
    ----------
    data: array or series
        the data to draw the distribution for

    """
    plt.figure(figsize=(8,6))


    x = data

    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, 
                                    gridspec_kw={"height_ratios": (.15, .85)})

    sns.boxplot(x, ax=ax_box)
    sns.distplot(x, ax=ax_hist, bins=n_bins, kde=False)

    ax_box.set(yticks=[])
    sns.despine(ax=ax_hist)
    sns.despine(ax=ax_box, left=True)
    plt.show()