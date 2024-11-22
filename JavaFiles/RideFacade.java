package JavaFiles;
// RideFacade.java
public class RideFacade {
    public double getFare(String serviceType, double distance) {
        RideService rideService;

        switch (serviceType.toLowerCase()) {
            case "carpool":
                rideService = new CarPOOLService();
                break;
            case "carx":
                rideService = new CarXService();
                break;
            case "carblack":
                rideService = new CarBlackService();
                break;
            default:
                throw new IllegalArgumentException("Unknown service type: " + serviceType);
        }

        return rideService.calculateFare(distance);
    }
}
