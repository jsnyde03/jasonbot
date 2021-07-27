from bs4 import BeautifulSoup
import requests
import json

query = {
"operationName": "ContentPageQuery",
  "variables": {
    "page": 1,
    "isPaginated": False,
    "perPage": 500,
    "sort": {
      "key": "FEATURED",
      "direction": "DESC"
    },
    "filters": [],
    "slug": "/categories/new-sets-and-products"
  },
  "query": "query ContentPageQuery($slug: String!, $perPage: Int, $page: Int, $isPaginated: Boolean!, $sort: SortInput, $filters: [Filter!]) {\n  contentPage(slug: $slug) {\n    id\n    analyticsGroup\n    analyticsPageTitle\n    metaTitle\n    metaDescription\n    metaOpenGraph {\n      title\n      description\n      imageUrl\n      __typename\n    }\n    url\n    title\n    displayTitleOnPage\n    ...Breadcrumbs\n    sections {\n      ... on LayoutSection {\n        ...PageLayoutSection\n        __typename\n      }\n      ...ContentSections\n      ... on TargetedSection {\n        fetchOnClient\n        section {\n          ...ContentSections\n          ... on LayoutSection {\n            ...PageLayoutSection\n            __typename\n          }\n          ... on ProductCarouselSection {\n            ...ProductCarousel_UniqueFields\n            productCarouselProducts: products(page: 1, perPage: 16, sort: $sort) {\n              ...Product_ProductItem\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      ... on SplitTestingSection {\n        variantId\n        testId\n        optimizelyEntityId\n        inExperimentAudience\n        section {\n          ...ContentSections\n          ... on LayoutSection {\n            ...PageLayoutSection\n            __typename\n          }\n          ... on ProductCarouselSection {\n            ...ProductCarousel_UniqueFields\n            productCarouselProducts: products(page: 1, perPage: 16, sort: $sort) {\n              ...Product_ProductItem\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      ... on ProductSection {\n        removePadding\n        ... on DisruptorProductSection {\n          ...DisruptorSection\n          __typename\n        }\n        ... on CountdownProductSection {\n          ...CountdownSection\n          __typename\n        }\n        products(perPage: $perPage, page: $page, sort: $sort, filters: $filters) @include(if: $isPaginated) {\n          ...ProductListings\n          __typename\n        }\n        products(page: $page, perPage: $perPage, sort: $sort, filters: $filters) @skip(if: $isPaginated) {\n          ...ProductListings\n          __typename\n        }\n        __typename\n      }\n      ... on ProductCarouselSection {\n        ...ProductCarousel_UniqueFields\n        productCarouselProducts: products(page: 1, perPage: 16, sort: $sort) {\n          ...Product_ProductItem\n          __typename\n        }\n        __typename\n      }\n      ... on CustomProductCarouselSection {\n        ...CustomProductCarousel_UniqueFields\n        productCarouselProducts: products(page: 1, perPage: 16, sort: $sort) {\n          ...CustomProductCarousel_ItemFields\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ContentSections on ContentSection {\n  __typename\n  id\n  ...UserGeneratedContentData\n  ...AccordionSectionData\n  ...BreadcrumbSection\n  ...CategoryListingSection\n  ...ListingBannerSection\n  ...CardContentSection\n  ...CardCarouselSection\n  ...CopyContent\n  ...CopySectionData\n  ...QuickLinksData\n  ...ContentBlockMixedData\n  ...HeroBannerData\n  ...MotionBannerData\n  ...MotionSidekickData\n  ...InPageNavData\n  ...GalleryData\n  ...TableData\n  ...RecommendationSectionData\n  ...SidekickBannerData\n  ...TextBlockData\n  ...TextBlockSEOData\n  ...CountdownBannerData\n  ...CrowdTwistWidgetSection\n  ...CodedSection\n  ...GridSectionData\n  ...StickyCTAData\n  ...AudioSectionData\n  ...MotionSidekick1x1Data\n  ...ImageTransitionSliderData\n  ...PollsSectionData\n  ...ArtNavigationData\n  ...MotionBanner16x9Data\n}\n\nfragment AccordionSectionData on AccordionSection {\n  __typename\n  id\n  title\n  showTitle\n  accordionBlocks {\n    title\n    text\n    __typename\n  }\n}\n\nfragment PageLayoutSection on LayoutSection {\n  __typename\n  id\n  backgroundColor\n  removePadding\n  fullWidth\n  innerSection: section {\n    id\n    ...ContentSections\n    ... on ProductCarouselSection {\n      ...ProductCarousel_UniqueFields\n      productCarouselProducts: products(page: 1, perPage: 16, sort: $sort) {\n        ...Product_ProductItem\n        __typename\n      }\n      __typename\n    }\n    ... on CustomProductCarouselSection {\n      ...CustomProductCarousel_UniqueFields\n      productCarouselProducts: products(page: 1, perPage: 16, sort: $sort) {\n        ...CustomProductCarousel_ItemFields\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment BreadcrumbSection on BreadcrumbSection {\n  ...BreadcrumbDynamicSection\n  __typename\n}\n\nfragment BreadcrumbDynamicSection on BreadcrumbSection {\n  breadcrumbs {\n    label\n    url\n    analyticsTitle\n    __typename\n  }\n  __typename\n}\n\nfragment ListingBannerSection on ListingBannerSection {\n  ...ListingBanner\n  __typename\n}\n\nfragment ListingBanner on ListingBannerSection {\n  title\n  description\n  contrast\n  logoImage\n  backgroundImages {\n    small {\n      ...ImageAsset\n      __typename\n    }\n    medium {\n      ...ImageAsset\n      __typename\n    }\n    large {\n      ...ImageAsset\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ImageAsset on ImageAssetDetails {\n  url\n  width\n  height\n  maxPixelDensity\n  format\n  __typename\n}\n\nfragment CategoryListingSection on CategoryListingSection {\n  ...CategoryListing\n  __typename\n}\n\nfragment CategoryListing on CategoryListingSection {\n  title\n  description\n  thumbnailImage\n  children {\n    ...CategoryLeafSection\n    __typename\n  }\n  __typename\n}\n\nfragment CategoryLeafSection on CategoryListingChildren {\n  title\n  description\n  thumbnailImage\n  logoImage\n  url\n  ageRange\n  tag\n  thumbnailSrc {\n    ...ImageAsset\n    __typename\n  }\n  __typename\n}\n\nfragment DisruptorSection on DisruptorProductSection {\n  disruptor {\n    ...DisruptorData\n    __typename\n  }\n  __typename\n}\n\nfragment DisruptorData on Disruptor {\n  __typename\n  imageSrc {\n    ...ImageAsset\n    __typename\n  }\n  contrast\n  background\n  title\n  description\n  link\n  openInNewTab\n}\n\nfragment ProductListings on ProductQueryResult {\n  count\n  offset\n  total\n  optimizelyExperiment {\n    testId\n    variantId\n    __typename\n  }\n  results {\n    ...Product_ProductItem\n    __typename\n  }\n  facets {\n    ...Facet_FacetSidebar\n    __typename\n  }\n  sortOptions {\n    ...Sort_SortOptions\n    __typename\n  }\n  __typename\n}\n\nfragment Product_ProductItem on Product {\n  __typename\n  id\n  productCode\n  name\n  slug\n  primaryImage(size: THUMBNAIL)\n  baseImgUrl: primaryImage\n  overrideUrl\n  ... on ReadOnlyProduct {\n    readOnlyVariant {\n      ...Variant_ReadOnlyProduct\n      __typename\n    }\n    __typename\n  }\n  ... on SingleVariantProduct {\n    variant {\n      ...Variant_ListingProduct\n      __typename\n    }\n    __typename\n  }\n  ... on MultiVariantProduct {\n    priceRange {\n      formattedPriceRange\n      formattedListPriceRange\n      __typename\n    }\n    variants {\n      ...Variant_ListingProduct\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment Variant_ListingProduct on ProductVariant {\n  id\n  sku\n  salePercentage\n  attributes {\n    rating\n    maxOrderQuantity\n    availabilityStatus\n    availabilityText\n    vipAvailabilityStatus\n    vipAvailabilityText\n    canAddToBag\n    canAddToWishlist\n    vipCanAddToBag\n    onSale\n    isNew\n    ...ProductAttributes_Flags\n    __typename\n  }\n  ...ProductVariant_Pricing\n  __typename\n}\n\nfragment ProductVariant_Pricing on ProductVariant {\n  price {\n    formattedAmount\n    centAmount\n    currencyCode\n    formattedValue\n    __typename\n  }\n  listPrice {\n    formattedAmount\n    centAmount\n    __typename\n  }\n  attributes {\n    onSale\n    __typename\n  }\n  __typename\n}\n\nfragment ProductAttributes_Flags on ProductAttributes {\n  featuredFlags {\n    key\n    label\n    __typename\n  }\n  __typename\n}\n\nfragment Variant_ReadOnlyProduct on ReadOnlyVariant {\n  id\n  sku\n  attributes {\n    featuredFlags {\n      key\n      label\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment Facet_FacetSidebar on Facet {\n  name\n  key\n  id\n  labels {\n    __typename\n    displayMode\n    name\n    labelKey\n    count\n    ... on FacetValue {\n      value\n      __typename\n    }\n    ... on FacetRange {\n      from\n      to\n      __typename\n    }\n  }\n  __typename\n}\n\nfragment Sort_SortOptions on SortOptions {\n  id\n  key\n  direction\n  label\n  __typename\n}\n\nfragment CardContentSection on CardContentSection {\n  ...CardContent\n  __typename\n}\n\nfragment CardContent on CardContentSection {\n  moduleTitle\n  showModuleTitle\n  blocks {\n    title\n    isH1\n    description\n    textAlignment\n    primaryLogoSrc {\n      ...ImageAsset\n      __typename\n    }\n    secondaryLogoSrc {\n      ...ImageAsset\n      __typename\n    }\n    logoPosition\n    imageSrc {\n      ...ImageAsset\n      __typename\n    }\n    callToActionText\n    callToActionLink\n    altText\n    contrast\n    videoMedia {\n      url\n      id\n      isLiveStream\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment CardCarouselSection on CardCarouselSection {\n  ...CardCarouselContent\n  __typename\n}\n\nfragment CardCarouselContent on CardCarouselSection {\n  moduleTitle\n  showModuleTitle\n  blocks {\n    title\n    isH1\n    description\n    textAlignment\n    primaryLogoSrc {\n      ...ImageAsset\n      __typename\n    }\n    secondaryLogoSrc {\n      ...ImageAsset\n      __typename\n    }\n    logoPosition\n    imageSrc {\n      ...ImageAsset\n      __typename\n    }\n    callToActionText\n    callToActionLink\n    altText\n    contrast\n    videoMedia {\n      url\n      id\n      isLiveStream\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment CopyContent on CopyContentSection {\n  blocks {\n    title\n    body\n    textAlignment\n    titleColor\n    imageSrc {\n      ...ImageAsset\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment CopySectionData on CopySection {\n  title\n  showTitle\n  body\n  __typename\n}\n\nfragment QuickLinksData on QuickLinkSection {\n  title\n  quickLinks {\n    title\n    isH1\n    link\n    openInNewTab\n    contrast\n    imageSrc {\n      ...ImageAsset\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ContentBlockMixedData on ContentBlockMixed {\n  moduleTitle\n  showModuleTitle\n  blocks {\n    title\n    isH1\n    description\n    backgroundColor\n    blockTheme\n    contentPosition\n    logoURL\n    logoPosition\n    callToActionText\n    callToActionLink\n    altText\n    backgroundImages {\n      largeImage {\n        small {\n          ...ImageAsset\n          __typename\n        }\n        large {\n          ...ImageAsset\n          __typename\n        }\n        __typename\n      }\n      smallImage {\n        small {\n          ...ImageAsset\n          __typename\n        }\n        large {\n          ...ImageAsset\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment UserGeneratedContentData on UserGeneratedContent {\n  ugcBlock {\n    title\n    text\n    ugcType\n    ugcKey\n    __typename\n  }\n  __typename\n}\n\nfragment HeroBannerData on HeroBanner {\n  heroblocks {\n    id\n    title\n    isH1\n    tagline\n    bannerTheme\n    contentVerticalPosition\n    contentHorizontalPosition\n    contentHeight\n    primaryLogoSrcNew {\n      ...ImageAsset\n      __typename\n    }\n    secondaryLogoSrcNew {\n      ...ImageAsset\n      __typename\n    }\n    videoMedia {\n      url\n      id\n      isLiveStream\n      __typename\n    }\n    logoPosition\n    contentBackground\n    callToActionText\n    callToActionLink\n    secondaryCallToActionText\n    secondaryCallToActionLink\n    secondaryOpenInNewTab\n    backgroundImagesNew {\n      small {\n        ...ImageAsset\n        __typename\n      }\n      medium {\n        ...ImageAsset\n        __typename\n      }\n      large {\n        ...ImageAsset\n        __typename\n      }\n      __typename\n    }\n    altText\n    __typename\n  }\n  __typename\n}\n\nfragment GalleryData on Gallery {\n  galleryblocks {\n    id\n    contentHeight\n    primaryLogoSrcNew {\n      ...ImageAsset\n      __typename\n    }\n    videoMedia {\n      url\n      id\n      isLiveStream\n      __typename\n    }\n    backgroundImagesNew {\n      small {\n        ...ImageAsset\n        __typename\n      }\n      medium {\n        ...ImageAsset\n        __typename\n      }\n      large {\n        ...ImageAsset\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment MotionBannerData on MotionBanner {\n  motionBannerBlocks {\n    id\n    title\n    isH1\n    tagline\n    bannerTheme\n    contentHorizontalPosition\n    primaryLogoSrc {\n      ...ImageAsset\n      __typename\n    }\n    secondaryLogoSrc {\n      ...ImageAsset\n      __typename\n    }\n    animatedMedia\n    videoMedia {\n      url\n      id\n      isLiveStream\n      __typename\n    }\n    logoPosition\n    contentBackground\n    callToActionText\n    callToActionLink\n    backgroundImages {\n      small {\n        ...ImageAsset\n        __typename\n      }\n      medium {\n        ...ImageAsset\n        __typename\n      }\n      large {\n        ...ImageAsset\n        __typename\n      }\n      __typename\n    }\n    altText\n    __typename\n  }\n  __typename\n}\n\nfragment MotionSidekickData on MotionSidekick {\n  motionSidekickBlocks {\n    id\n    title\n    isH1\n    tagline\n    bannerTheme\n    contentHorizontalPosition\n    primaryLogoSrc {\n      ...ImageAsset\n      __typename\n    }\n    secondaryLogoSrc {\n      ...ImageAsset\n      __typename\n    }\n    animatedMedia\n    videoMedia {\n      url\n      id\n      isLiveStream\n      __typename\n    }\n    logoPosition\n    contentBackground\n    callToActionText\n    callToActionLink\n    backgroundImages {\n      small {\n        ...ImageAsset\n        __typename\n      }\n      medium {\n        ...ImageAsset\n        __typename\n      }\n      large {\n        ...ImageAsset\n        __typename\n      }\n      __typename\n    }\n    altText\n    __typename\n  }\n  __typename\n}\n\nfragment InPageNavData on InPageNav {\n  inPageNavBlocks {\n    id\n    title\n    isH1\n    text\n    contrast\n    primaryLogoSrc\n    secondaryLogoSrc\n    animatedMedia\n    videoMedia {\n      url\n      id\n      __typename\n    }\n    contentBackground\n    backgroundImages {\n      small\n      medium\n      large\n      __typename\n    }\n    callToActionText\n    callToActionLink\n    openInNewTab\n    secondaryCallToActionText\n    secondaryCallToActionLink\n    secondaryOpenInNewTab\n    __typename\n  }\n  __typename\n}\n\nfragment TableData on TableSection {\n  rows {\n    isHeadingRow\n    cells\n    __typename\n  }\n  __typename\n}\n\nfragment RecommendationSectionData on RecommendationSection {\n  __typename\n  title\n  showTitle\n  recommendationType\n}\n\nfragment SidekickBannerData on SidekickBanner {\n  __typename\n  id\n  sidekickBlocks {\n    title\n    isH1\n    text\n    textAlignment\n    contrast\n    backgroundColor\n    logoSrc {\n      ...ImageAsset\n      __typename\n    }\n    secondaryLogoSrc {\n      ...ImageAsset\n      __typename\n    }\n    logoPosition\n    ctaTextPrimary: ctaText\n    ctaLinkPrimary: ctaLink\n    ctaTextSecondary\n    ctaLinkSecondary\n    contentHeight\n    bgImages {\n      large\n      __typename\n    }\n    videoMedia {\n      url\n      id\n      isLiveStream\n      __typename\n    }\n    altText\n    __typename\n  }\n}\n\nfragment ProductCarousel_UniqueFields on ProductCarouselSection {\n  __typename\n  productCarouselTitle: title\n  showTitle\n  showAddToBag\n  seeAllLink\n}\n\nfragment CustomProductCarousel_UniqueFields on CustomProductCarouselSection {\n  __typename\n  productCarouselTitle: title\n  showTitle\n  showAddToBag\n  seeAllLink\n  backgroundColor\n}\n\nfragment CustomProductCarousel_ItemFields on CustomProductCarouselItem {\n  product {\n    ...Product_ProductItem\n    __typename\n  }\n  imageOverride {\n    ...ImageAsset\n    __typename\n  }\n  imageBackgroundColor\n  contentBackgroundColor\n  ctaButtonColor\n  __typename\n}\n\nfragment TextBlockData on TextBlock {\n  textBlocks {\n    title\n    isH1\n    text\n    textAlignment\n    contrast\n    backgroundColor\n    callToActionLink\n    callToActionText\n    openInNewTab\n    secondaryCallToActionLink\n    secondaryCallToActionText\n    secondaryOpenInNewTab\n    __typename\n  }\n  __typename\n}\n\nfragment TextBlockSEOData on TextBlockSEO {\n  textBlocks {\n    title\n    text\n    __typename\n  }\n  __typename\n}\n\nfragment Countdown on CountdownBannerChild {\n  title\n  isH1\n  text\n  textPosition\n  textAlignment\n  contrast\n  backgroundColor\n  callToActionLink\n  callToActionText\n  openInNewTab\n  countdownDate\n  __typename\n}\n\nfragment CountdownBannerData on CountdownBanner {\n  countdownBannerBlocks {\n    ...Countdown\n    __typename\n  }\n  __typename\n}\n\nfragment CountdownSection on CountdownProductSection {\n  countdown {\n    ...Countdown\n    __typename\n  }\n  __typename\n}\n\nfragment CrowdTwistWidgetSection on CrowdTwistWidgetSection {\n  __typename\n  id\n  heading\n  activityId\n  rewardId\n}\n\nfragment CodedSection on CodedSection {\n  __typename\n  id\n  componentName\n  properties {\n    key\n    value\n    __typename\n  }\n  text {\n    key\n    value\n    __typename\n  }\n  media {\n    key\n    values {\n      id\n      contentType\n      fileSize\n      filename\n      url\n      title\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment GridSectionData on GridSection {\n  items {\n    id\n    image\n    videoMedia {\n      id\n      url\n      isLiveStream\n      __typename\n    }\n    href\n    text\n    textContrast\n    __typename\n  }\n  __typename\n}\n\nfragment AudioSectionData on AudioSection {\n  tracks {\n    trackArt {\n      ...ImageAsset\n      __typename\n    }\n    src\n    title\n    description\n    __typename\n  }\n  backgroundColor\n  textContrast\n  backgroundImage {\n    mobile {\n      ...ImageAsset\n      __typename\n    }\n    desktop {\n      ...ImageAsset\n      __typename\n    }\n    __typename\n  }\n  seriesTitle\n  seriesThumbnail {\n    ...ImageAsset\n    __typename\n  }\n  __typename\n}\n\nfragment Breadcrumbs on Content {\n  breadcrumbs {\n    __typename\n    label\n    url\n    analyticsTitle\n  }\n  __typename\n}\n\nfragment StickyCTAData on StickyCTASection {\n  item {\n    backgroundColor\n    ctaBackgroundImage\n    ctaPosition\n    href\n    text\n    textAlign\n    textContrast\n    __typename\n  }\n  __typename\n}\n\nfragment MotionSidekick1x1Data on MotionSidekick1x1 {\n  motionSidekickBlocks {\n    id\n    title\n    description\n    textContrast\n    contentHorizontalPosition\n    primaryLogoSrc {\n      ...ImageAsset\n      __typename\n    }\n    secondaryLogoSrc {\n      ...ImageAsset\n      __typename\n    }\n    inlineVideo {\n      id\n      url\n      isLiveStream\n      __typename\n    }\n    fullVideo {\n      id\n      url\n      isLiveStream\n      __typename\n    }\n    logoHorizontalPosition\n    backgroundColor\n    primaryCallToActionText\n    primaryCallToActionLink\n    secondaryCallToActionText\n    secondaryCallToActionLink\n    __typename\n  }\n  __typename\n}\n\nfragment ImageTransitionSliderData on ImageTransitionSlider {\n  imageTransitionSliderBlocks {\n    id\n    title\n    description\n    backgroundColor\n    contrast\n    ctas {\n      link\n      text\n      __typename\n    }\n    contentHorizontalPosition\n    firstImage {\n      ...ImageAsset\n      __typename\n    }\n    secondImage {\n      ...ImageAsset\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PollsSectionData on PollsSection {\n  id\n  question\n  backgroundColor\n  answerFillColor\n  answerBorderColor\n  answers {\n    answer\n    id\n    __typename\n  }\n  textContrast\n  image {\n    ...ImageAsset\n    __typename\n  }\n  imageAlignment\n  pollResults {\n    answers {\n      answerId\n      count\n      __typename\n    }\n    totalVotes\n    __typename\n  }\n  __typename\n}\n\nfragment ArtNavigationData on ArtNavigation {\n  artNavigationBlocks {\n    id\n    title\n    callToActionLink\n    backgroundImage {\n      ...ImageAsset\n      __typename\n    }\n    logoImage {\n      ...ImageAsset\n      __typename\n    }\n    textImage {\n      ...ImageAsset\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment MotionBanner16x9Data on MotionBanner16x9 {\n  motionBannerBlocks {\n    id\n    title\n    isH1\n    tagline\n    contentHorizontalPosition\n    primaryLogoSrc {\n      ...ImageAsset\n      __typename\n    }\n    secondaryLogoSrc {\n      ...ImageAsset\n      __typename\n    }\n    animatedMedia\n    videoMedia {\n      url\n      id\n      isLiveStream\n      __typename\n    }\n    logoPosition\n    contentBackground\n    callToActionText\n    callToActionLink\n    altText\n    __typename\n  }\n  __typename\n}\n"
}
def find_products(shop):
  print(shop)
  url = "https://www.lego.com/api/graphql/ContentPageQuery"
  headers = {
        "Content-Type": "application/json",
        "x-locale": "en-US"
    }
  request = requests.post(url, json=query, headers=headers)
  shop_products = request.json()["data"]["contentPage"]["sections"][3]["products"]["results"]
  products = []
  for product in shop_products:
    if(product["__typename"]) == "SingleVariantProduct":
        products.insert(0, {
          "title": product["name"],
          "price": product["variant"]["price"]["formattedAmount"],
          "availability": product["variant"]["attributes"]["availabilityText"],
          "vip": product["variant"]["attributes"]["vipAvailabilityText"],
          "image": product["primaryImage"],
          "url": "https://www.lego.com/en-us/product" +product["slug"]
       })
  return products