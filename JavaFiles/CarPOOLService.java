package JavaFiles;
public class CarPOOLService extends RideService {
    public CarPOOLService() {
        super(new CarPOOLStrategy());
    }

    @Override
    public double calculateFare(double distance) {
        return pricingStrategy.calculateFare(distance);
    }
}