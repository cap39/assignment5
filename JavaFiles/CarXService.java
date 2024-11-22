package JavaFiles;
public class CarXService extends RideService {
    public CarXService() {
        super(new CarXStrategy());
    }

    @Override
    public double calculateFare(double distance) {
        return pricingStrategy.calculateFare(distance);
    }
}