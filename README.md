# news_explainer
A classifier that will classify news according to topics based on either the headline or a short excerpt of the news article.

Look at Jupyter Notebook for the implementation of the explainer as well as a few examples that are tested on the model.

## Examples
### Correctly categorized headline
**Headline:** 
ICE Renews Private Prison Contractor to Run Largest Family Detention Center. The
renewal came despite a Department of Homeland Security order to review
whether the agency should keep running its facilities as for profit businesses.

![Probability list of words for correctly categorized headline](https://github.com/karyiteh/news_explainer/blob/master/images/correct_prob.png)
![Probability plot of words for correctly categorized headline](https://github.com/karyiteh/news_explainer/blob/master/images/correct_plot.png)
![Text highlight of words that explain categories for correctly categorized headline](https://github.com/karyiteh/news_explainer/blob/master/images/correct_highlight.png)

### Wrongly categorized headline
**Headline:** 
Trump’s Tariff Tirade Makes More Sense After You Watch ‘Mean Girls’. That
explains everything!

**Actual category:**
Politics

![Probability list of words for wrongly categorized headline](https://github.com/karyiteh/news_explainer/blob/master/images/wrong_prob.png)
![Probability plot of words for wrongly categorized headline](https://github.com/karyiteh/news_explainer/blob/master/images/wrong_plot.png)
![Text highlight of words that explain categories for wrongly categorized headline](https://github.com/karyiteh/news_explainer/blob/master/images/wrong_highlight.png)

### Headline where model is uncertain
**Headline:** 
The Fairest (Skin) Of Them All. I think I always knew that being pale in a tan
worshipping world was an uphill climb.

**Actual category:**
Style & Beauty

![Probability list of words for uncertain categorized headline](https://github.com/karyiteh/news_explainer/blob/master/images/uncertain_prob.png)
![Probability list of words for uncertain categorized headline](https://github.com/karyiteh/news_explainer/blob/master/images/uncertain_prob2.png)
![Probability plot of words for uncertain categorized headline](https://github.com/karyiteh/news_explainer/blob/master/images/uncertain_plot.png)
![Text highlight of words that explain categories for uncertain categorized headline](https://github.com/karyiteh/news_explainer/blob/master/images/uncertain_highlight.png)
