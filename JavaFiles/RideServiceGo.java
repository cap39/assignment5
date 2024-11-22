package JavaFiles;

public interface RideServiceGo extends Cloneable {
    RideServiceGo cloneService();
    void setServiceDetails(String details);
    String getServiceDetails();
}