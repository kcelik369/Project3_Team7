
CREATE TABLE hosts (
    host_id INT  PRIMARY KEY,
    host_since DATE  NOT NULL,
    host_location VARCHAR   NOT NULL,
    host_response_time VARCHAR   NOT NULL,
    host_response_rate FLOAT   NOT NULL,
    host_acceptance_rate FLOAT   NOT NULL,
    host_is_superhost BOOLEAN   NOT NULL,
    host_neighbourhood VARCHAR   NOT NULL,
    host_listings_count FLOAT   NOT NULL,
    host_verifications_count INT   NOT NULL,
    host_has_profile_pic BOOLEAN   NOT NULL,
    host_identity_verified BOOLEAN   NOT NULL
);


CREATE TABLE property_avg_pricing (
    property_type VARCHAR   NOT NULL,
    neighbourhood VARCHAR   NOT NULL,
    price FLOAT  NOT NULL,

    PRIMARY KEY (property_type,  neighbourhood)-- Composite primary key
);


CREATE TABLE listings_cleaned (
    id INT   PRIMARY KEY,
    name VARCHAR   NOT NULL,
    host_id INT   NOT NULL,
    street VARCHAR   NOT NULL,
    neighbourhood VARCHAR   NOT NULL,
    zipcode VARCHAR   NOT NULL,
    property_type VARCHAR   NOT NULL,
    room_type VARCHAR   NOT NULL,
    accommodates INT   NOT NULL,
    bathrooms FLOAT   NOT NULL,
    bedrooms FLOAT   NOT NULL,
    beds FLOAT   NOT NULL,
    bed_type VARCHAR   NOT NULL,
    amenities_count INT   NOT NULL,
    price FLOAT   NOT NULL,
    weekly_price FLOAT   NOT NULL,
    monthly_price FLOAT   NOT NULL,
    security_deposit FLOAT   NOT NULL,
    cleaning_fee FLOAT   NOT NULL,
    guests_included INT   NOT NULL,
    extra_people FLOAT   NOT NULL,
    minimum_nights INT   NOT NULL,
    maximum_nights INT   NOT NULL,
    instant_bookable BOOLEAN   NOT NULL,
    cancellation_policy VARCHAR   NOT NULL,
    require_guest_profile_picture BOOLEAN   NOT NULL,
    require_guest_phone_verification BOOLEAN   NOT NULL,
    avg_availability FLOAT   NOT NULL,
	
	
);

CREATE TABLE listing_scores (
	score_id SERIAL PRIMARY KEY,
    id INT NOT NULL,
    number_of_reviews INT   NOT NULL,
    review_scores_rating INT   NOT NULL,
    review_scores_accuracy INT   NOT NULL,
    review_scores_cleanliness INT   NOT NULL,
    review_scores_checkin INT   NOT NULL,
    review_scores_communication INT   NOT NULL,
    review_scores_location INT   NOT NULL,
    review_scores_value INT   NOT NULL,
    reviews_per_month FLOAT   NOT NULL,
	
	FOREIGN KEY (id) REFERENCES listings_cleaned(id)
);


CREATE TABLE calendar_average_pricing (
    
	listing_id INT NOT NULL,
    month INT   NOT NULL,
    price FLOAT   NOT NULL,

    FOREIGN KEY (listing_id) REFERENCES listings_cleaned(id)
);


