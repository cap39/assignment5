package JavaFiles;

// CarGoService.java
public class CarGoService implements RideServiceGo {
    private String serviceDetails;

    @Override
    public RideServiceGo cloneService() {
        CarGoService clone = null;
        try {
            clone = (CarGoService) super.clone();
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
        return "CarGo Service: " + serviceDetails;
    }
}

