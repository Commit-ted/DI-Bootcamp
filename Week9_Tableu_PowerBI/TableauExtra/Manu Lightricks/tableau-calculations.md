# User Acquisition Metrics

## Conversion Metrics
```
// Funnel Conversion Rate
[Installs] / [Impressions] * 100

// Install to Purchase Rate
[Purchases] / [Installs] * 100

// Click to Install Rate
[Installs] / ([CTR (%)] * [Impressions] / 100) * 100

// Cost Recovery Time (Days)
[CPI ($)] / ([revenue] / [Purchases]) * 30
```

## Efficiency Metrics
```
// eCPM (Effective Cost Per Mille)
[Spend] / [Impressions] * 1000

// Cost Per Engaged User
[Spend] / [Post Engagement]

// Revenue Per Install
[revenue] / [Installs]

// Marketing Efficiency Ratio
[revenue] / [Spend]
```

## Video Performance
```
// Viewer Drop-off Rate
(([3sec Video View Rate (%)] - [100% Video View Rate (%)]) / [3sec Video View Rate (%)] * 100)

// Video Engagement Score
([25% Video View Rate (%)] * 0.25 + 
 [50% Video View Rate (%)] * 0.5 + 
 [75% Video View Rate (%)] * 0.75 + 
 [100% Video View Rate (%)] * 1) / 2.5

// Video Completion Quality
[100% Video View Rate (%)] / [3sec Video View Rate (%)] * 100
```

## ROI Analysis
```
// Customer Acquisition Cost (CAC)
[Spend] / [Purchases]

// Lifetime Value (LTV) Proxy
[revenue] / [Purchases]

// LTV to CAC Ratio
([revenue] / [Purchases]) / ([Spend] / [Purchases])

// Break-Even Analysis
[CPI ($)] / ([revenue] / [Installs])
```

## Campaign Health Indicators
```
// Campaign Efficiency Index
(([Installs] / [Impressions]) * [ROAS] * 100) / [CPI ($)]

// Engagement Quality Score
([Post Engagement] / [Impressions] * 0.3 + 
 [Video Views] / [Impressions] * 0.3 + 
 [Installs] / [Impressions] * 0.4) * 100

// Creative Fatigue Indicator
// Use with time series data
(PREVIOUS_VALUE([CTR (%)]) - [CTR (%)]) / PREVIOUS_VALUE([CTR (%)])
```

## Segmentation & Analysis
```
// Campaign Performance Tier
CASE 
    WHEN [ROAS] >= 1 AND [Install Rate (%)] > AVG([Install Rate (%)]) 
        THEN 'High Performer'
    WHEN [ROAS] >= 1 AND [Install Rate (%)] <= AVG([Install Rate (%)]) 
        THEN 'Efficient'
    WHEN [ROAS] < 1 AND [Install Rate (%)] > AVG([Install Rate (%)]) 
        THEN 'Volume Driver'
    ELSE 'Needs Optimization'
END

// Scale Efficiency
CASE 
    WHEN [Spend] > AVG([Spend]) AND [ROAS] > AVG([ROAS]) 
        THEN 'Scale Champion'
    WHEN [Spend] > AVG([Spend]) AND [ROAS] <= AVG([ROAS]) 
        THEN 'Scale Challenge'
    WHEN [Spend] <= AVG([Spend]) AND [ROAS] > AVG([ROAS]) 
        THEN 'Growth Opportunity'
    ELSE 'Testing Phase'
END

// Creative Type Performance
CASE 
    WHEN [Video Views] / NULLIF([Impressions],0) > 0.5 
        THEN 'Video Dominant'
    WHEN [Post Engagement] / NULLIF([Impressions],0) > 0.3 
        THEN 'Engagement Driven'
    ELSE 'Direct Response'
END
```

## Advanced Analysis
```
// User Quality Index
([Purchases] / NULLIF([Installs],0) * 0.4 + 
 [revenue] / NULLIF([Installs],0) * 0.4 + 
 [Post Engagement] / NULLIF([Impressions],0) * 0.2) * 100

// Relative Campaign Performance
([ROAS] - AVG([ROAS])) / STDEV([ROAS])

// ROI Efficiency Score
(([ROAS] / AVG([ROAS]) * 0.4) + 
 ([Install Rate (%)] / AVG([Install Rate (%)]) * 0.3) + 
 ([CTR (%)] / AVG([CTR (%)]) * 0.3)) * 100
```
