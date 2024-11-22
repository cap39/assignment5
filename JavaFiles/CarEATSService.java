package JavaFiles;

// CarEATSService.java
public class CarEATSService implements RideServiceGo {
    private String serviceDetails;

    @Override
    public RideServiceGo cloneService() {
        CarEATSService clone = null;
        try {
            clone = (CarEATSService) super.clone();
        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
        }
        return clone;
    }

    @Override
    public void setServiceDetails(String details) {
        this.serviceDetails = details;
    }

    @Override
    public String getServiceDetails() {
        return "CarEATS Service: " + serviceDetails;
    }
}